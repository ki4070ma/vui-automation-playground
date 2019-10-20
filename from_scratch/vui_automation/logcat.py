#!/usr/bin/env python

import queue
import subprocess as sp
import threading
import time


class Logcat(object):

    def log_clear(self):
        sp.run(["adb", "logcat", "-c"])

    def wait_for_word_in_log(self, word, timeout=10, log_clear=True):
        if log_clear:
            self.log_clear()

        process = sp.Popen(["adb", "logcat"], stdout=sp.PIPE)

        # Launch the asynchronous readers of the process' stdout.
        stdout_queue = queue.Queue()
        stdout_reader = AsynchronousFileReader(process.stdout, stdout_queue)
        stdout_reader.start()

        # Check the queues if we received some output (until there is nothing
        # more to get).
        found_flg = False
        print('waiting...')
        start = time.time()
        while not stdout_reader.eof() and not found_flg and time.time() - start < 10:
            while not stdout_queue.empty():
                line = str(stdout_queue.get())
                if word in line:
                    found_flg = True
                    print(line)
                    break
        if found_flg:
            print('***Found: {}'.format(word))
        else:
            print('***Not found: {}. Timeout: {}sec.'.format(word, timeout))
        stdout_reader.stop()


class AsynchronousFileReader(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a files
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


if __name__ == '__main__':
    logcat = Logcat()
    word = "ActivityManager: Displayed com.google.android.googlequicksearchbox/com.google.android.apps.gsa.staticplugins.opa.OpaActivity"
    logcat.wait_for_word_in_log(word)
