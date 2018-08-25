#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

import unittest
from cStringIO import StringIO
import sys

from ps4a import *
from ps4b import *

class TestPS4B_compChooserWord(unittest.TestCase):
    def setUp(self):
        old_stdout = sys.stdout
        # sys.stdout = mystdout = StringIO()
        sys.stdout = StringIO()
        self.wordList = loadWords()
        sys.stdout = old_stdout

    def test_1(self):
        hand = {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
        answer = 'appels'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)

    # @unittest.skip('')
    def test_2(self):
        hand = {'a': 2, 'c': 1, 'b': 1, 't': 1}
        answer = 'acta'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)

    # @unittest.skip('')
    def test_3(self):
        hand = {'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}
        answer = 'imamate'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)

    # @unittest.skip('')
    def test_4(self):
        hand = {'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}
        # answer = None
        self.assertIsNone(compChooseWord(hand, self.wordList))

    # @unittest.skip('')
    def test_5(self):
        hand = {'a': 1, 'd': 1, 'i': 1, 'k': 1, 'o': 1, 'n': 1, 'y': 1}
        answer = 'daikon'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)

    # @unittest.skip('')
    def test_6(self):
        hand = {'a': 2, 'd': 2, 'i': 2, 'k': 2, 'o': 2, 'n': 2}
        answer = 'dikdik'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)

    # @unittest.skip('')
    def test_7(self):
        hand = {'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}
        answer = 'aikido'
        self.assertEqual(compChooseWord(hand, self.wordList), answer)


class TestPS4B_compPlayHand(unittest.TestCase):
    def setUp(self):
        old_stdout = sys.stdout
        # sys.stdout = mystdout = StringIO()
        sys.stdout = StringIO()
        self.wordList = loadWords()
        sys.stdout = old_stdout
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_1(self):
        hand = {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
        answer = '''Current Hand:
a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.
'''
        compPlayHand(hand, self.wordList)
        self.assertEqual(sys.stdout.getvalue(), answer)

    # @unittest.skip('')
    def test_2(self):
        hand = {'a': 2, 'c': 1, 'b': 1, 't': 1}
        answer = '''Current Hand:
a a c b t
"acta" earned 24 points. Total: 24 points
Current Hand:
b
Total score: 24 points.
'''
        compPlayHand(hand, self.wordList)
        self.assertEqual(sys.stdout.getvalue(), answer)

    # @unittest.skip('')
    def test_3(self):
        hand = {'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}
        answer = '''Current Hand:
a a e e t t i i m m n n
"immanent" earned 96 points. Total: 96 points
Current Hand:
a e t i
"ait" earned 9 points. Total: 105 points
Current Hand:
e
Total score: 105 points.
'''
        compPlayHand(hand, self.wordList)
        self.assertEqual(sys.stdout.getvalue(), answer)


if __name__ == '__main__':
    unittest.main()
