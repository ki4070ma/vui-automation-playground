#!/usr/bin/python

import json
import os


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


class SentenceLoader(object):

    def __init__(self, filename=PATH('../files/sentences.json')):
        with open(filename) as fr:
            self.sentences_json = json.load(fr)

    def get_sentence_names(self):
        return self.sentences_json.keys()

    def get_sentence(self, name, locale):
        return self.sentences_json[name][locale]
