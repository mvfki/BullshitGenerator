#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

class bullShit():
    def __init__(self, jsonFile, theme, repeatLevel = 2, wordLimit = 1000):
        self.data = readJSON.readJsonFile(jsonFile)
        #self.famous = data['famous']
        self.before = self.data['before']
        self.after = self.data['after']
        #self.bosh = data['bosh']
        self.theme = theme
        self.essay = theme
        self.repeatLevel = repeatLevel
        #self.pool = list(self.famous) * 2
        self.famousGen = self._sentence('famous')
        #self.beforeGen = self._sentence('before')
        #self.afterGen = self._sentence('after')
        self.boshGen = self._sentence('bosh')
        self.POOPOO(wordLimit)

    def POOPOO(self, wordLimit):
        while len(self.essay) < wordLimit:
            dice = random.randint(0, 100)
            if dice < 5:
                self._nextParagraph()
            elif dice < 20:
                self._addFullSentence()
            else:
                self._addBosh()
        self.essay = self.essay.replace('x', self.theme)

    def _sentence(self, Type):
        pool = list(self.data[Type]) * self.repeatLevel
        while True:
            random.shuffle(pool)
            for i in pool:
                yield i

    def _addFullSentence(self):
        sentence = next(self.famousGen)
        sentence = sentence.replace('a', random.choice(self.before))
        sentence = sentence.replace('b', random.choice(self.after))
        self.essay += sentence

    def _addBosh(self):
        self.essay += next(self.boshGen)

    def _nextParagraph(self):
        self.essay += '。'
        self.essay += '\r\n'
        self.essay += '　　'

    def __str__(self):
        return self.essay

    def __repr__(self):
        return 'NMSL'

if __name__ == '__main__':
    import sys
    theme = sys.argv[1]
    bs = bullShit("data.json", theme)
    print(bs)
