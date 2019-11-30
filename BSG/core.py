#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import random, json

this_dir, this_filename = os.path.split(__file__)
_defaultData = os.path.join(this_dir, "default.json")
class bullShit():
    '''An object that can generate random bullShit.
    
    Arguments:
    -------------
    theme       - str. 
                  The main theme you want to discuss about
    jsonFile    - str, Optional, default None. 
                  A file that stores the famous words and boshes. By default, 
                  a basic data package would be loaded internally from this 
                  package.
    repeatLevel - int, Optional, default 2. 
    wordLimit   - int, Optional, default 1000.
    
    Returns:
    -------------
    Try print(bullShit(<theme>) to see what happens.
    '''
    def __init__(self, theme, jsonFile = None, 
                 repeatLevel = 2, wordLimit = 1000):
        if jsonFile == None:
            jsonFile = _defaultData
        self.data = json.loads(open(jsonFile, 'r', encoding = "utf-8").read())
        self.before = self.data['before']
        self.after = self.data['after']
        self.theme = theme
        self._wordLimit = wordLimit
        self.repeatLevel = repeatLevel
        self.famousGen = self._sentence('famous')
        self.boshGen = self._sentence('bosh')
        self.POOPOO(wordLimit)

    def POOPOO(self, wordLimit = None):
        '''Generate new paragraphs of bullShit. Is run once by default when 
        initializing, but can be applied whenever you what to get new stuffs.

        Argument:
        ------------
        wordLimit - int. Optional, default None. By default, it will use the 
                    intrinsic value specified when initializing this object.

        Returns:
        -----------
        Update the essay stored in the object. 
        '''
        self.essay = '　　'
        if wordLimit == None:
            wordLimit = self._wordLimit
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
        self.essay += '\r\n'
        self.essay += '　　'

    def __str__(self):
        return self.essay

    def __repr__(self):
        return 'NMSL'

if __name__ == '__main__':
    import sys
    theme = sys.argv[1]
    if len(sys.argv) > 2:
        wordLimit = int(sys.argv[2])
    else:
        wordLimit = 1000
    bs = bullShit("data.json", theme, wordLimit = wordLimit)
    print(bs)
