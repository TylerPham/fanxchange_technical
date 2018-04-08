import unittest
from word_counter import mostCommonWords, wordCount 

class test_word_counter(unittest.TestCase):

    def test_simple_wordCount(self):
        self.assertEqual(wordCount('simple.txt'), 15)
    
    def test_simple_mostCommonWords(self):
        self.assertEqual(mostCommonWords('simple.txt'), {'worda': 5, 'wordb':4, 'wordc':3, 'wordd':2, 'worde':1})

    def test_multiline_wordCount(self):
        self.assertEqual(wordCount('multiline.txt'), 15)
    
    def test_multiline_mostCommonWords(self):
        self.assertEqual(mostCommonWords('multiline.txt'), {'worda': 5, 'wordb':4, 'wordc':3, 'wordd':2, 'worde':1})

    def test_morethanten_wordCount(self):
        self.assertEqual(wordCount('morethanten.txt'), 21)
    
    def test_morethanten_mostCommonWords(self):
        self.assertEqual(mostCommonWords('morethanten.txt'), 
        {
        'word1': 2,
        'word2': 2,
        'word3': 2,
        'word4': 2,
        'word5': 2,
        'word6': 2,
        'word7': 2,
        'word8': 2,
        'word9': 2,
        'word10': 2,
        })

    def test_capitals_wordCount(self):
        self.assertEqual(wordCount('capitals.txt'), 15)
    
    def test_capitals_mostCommonWords(self):
        self.assertEqual(mostCommonWords('capitals.txt'), {'worda': 5, 'wordb':4, 'wordc':3, 'wordd':2, 'worde':1})

    def test_punctuation_wordCount(self):
        self.assertEqual(wordCount('punctuation.txt'), 15)
    
    def test_punctuation_mostCommonWords(self):
        self.assertEqual(mostCommonWords('punctuation.txt'), {'worda': 5, 'wordb':4, 'wordc':3, 'wordd':2, 'worde':1})

    def test_contractions_wordCount(self):
        self.assertEqual(wordCount('contractions.txt'), 3)
    
    def test_contractions_mostCommonWords(self):
        self.assertEqual(mostCommonWords('contractions.txt'), {"doesnt": 2, "isnt":1})


if __name__ == '__main__':
    unittest.main()