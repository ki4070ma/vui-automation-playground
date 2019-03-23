#!/usr/bin/env python

import queue
import subprocess
import threading


class AsynchronousFileReader(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a file
    in a separate thread. Pushes read lines on a queue to
    be consumed in another thread.
    '''

    def __init__(self, fd, q):
        assert isinstance(q, queue.Queue)
        assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._fd = fd
        self._queue = q
        self.stop_event = threading.Event()

    def run(self):
        '''The body of the tread: read lines and put them on the queue.'''
        for line in iter(self._fd.readline, ''):
            self._queue.put(line)
            if self.stop_event.is_set():
                break

    def eof(self):
        '''Check whether there is no more content to expect.'''
        return not self.is_alive() and self._queue.empty()

    def stop(self):
        self.stop_event.set()
        self.join()


# You'll need to add any command line arguments here.
process = subprocess.Popen(["adb", "logcat"], stdout=subprocess.PIPE)

# Launch the asynchronous readers of the process' stdout.
stdout_queue = queue.Queue()
stdout_reader = AsynchronousFileReader(process.stdout, stdout_queue)
stdout_reader.start()

# Check the queues if we received some output (until there is nothing more to get).
break_flg = False
while not stdout_reader.eof() and break_flg is False:
    while not stdout_queue.empty():
        line = str(stdout_queue.get())
        if 'HOGE' in line:
            print(line)
            break_flg = True
            break
print('Done')
stdout_reader.stop()
