import word_ladder
import unittest

wordList = ["the", "then", "hello", "hide", "say", "total", "seek"]
class TestLaddergram(unittest.TestCase):

    def test_getDictValid1(self):   # The file dict.txt contains the words "a few words" separated by new lines
        self.assertEqual(word_ladder.getDict("dict.txt"), ["a\n", "few\n", "words"])

    def test_getDictInvalid1(self): # The file dict2.txt is empty
        self.assertFalse(word_ladder.getDict("dict2.txt"))

    def test_getDictInvalid2(self):
        self.assertFalse(word_ladder.getDict("blah"))

    def test_getInputWordsValid1(self):
        self.assertEqual(word_ladder.getInputWords("hide", "seek", wordList), ["then", "hide", "seek"])

    def test_getInputWordsValid2(self):
        self.assertEqual(word_ladder.getInputWords("the", "say", wordList), ["the", "say"])

    def test_getInputWordsInvalid1(self): # Start & target not the same length
        self.assertFalse(word_ladder.getInputWords("the", "seek", wordList))

    def test_getInputWordsInvalid2(self): # Start word not in the wordList
        self.assertFalse(word_ladder.getInputWords("blah", "seek", wordList))

    def test_getInputWordsInvalid3(self): # Target word not in the wordList
        self.assertFalse(word_ladder.getInputWords("seek", "blah", wordList))

    def test_getInputWordsInvalid4(self): # Start & target are the same word
        self.assertFalse(word_ladder.getInputWords("seek", "seek", wordList))

    def test_getSeenDictValid1(self): # The file dict.txt contains "a few words" separated by new lines
        self.assertEqual(word_ladder.getSeenDict("dict.txt", "hide"), {"hide": True, "a": True, "few": True, "words": True})

    def test_getSeenDictInvalid1(self): # The file dict2.txt is empty
        self.assertFalse(word_ladder.getSeenDict("dict2.txt", "hide"))

    def test_getSeenDictInvalid2(self): # The file blah.txt doesn't exist
        self.assertFalse(word_ladder.getSeenDict("blah.txt", "hide"))

    def test_sameValid1(self):
        self.assertEqual(word_ladder.same("the", "say"), 0)

    def test_sameValid2(self):
        self.assertEqual(word_ladder.same("goal", "load"), 2)
    # The length of the start & target being equal has already been checked by previous functions

    def test_buildValid1(self):
        words = ['aide', 'bide', 'down', 'hide', 'loan', 'side', 'seek']
        seen = {"hide": True}
        list = []
        self.assertEqual(word_ladder.build(".ide", words, seen, list), ['aide', 'bide', 'side'])

    def test_buildValid2(self):
        words = ['coal', 'down', 'goal', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        seen = {"load": True}
        list = ['coal']
        self.assertEqual(word_ladder.build(".oal", words, seen, list), ['goal', 'foal'])
    # Previous functions make sure that no invalid inputs are given to the build function

    def test_shortestFindValid1(self):
        word = "lead"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        target = "gold"
        seen = {"lead": True}
        self.assertEqual(word_ladder.shortestFind(word, words, target, seen), (3, ['lead', 'load', 'goad', 'gold']))

    def test_shortestFindValid2(self):
        word = "hell"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        target = "gold"
        seen = {"lead": True}
        self.assertFalse(word_ladder.shortestFind(word, words, target, seen))
    # Previous functions make sure that the functions parameters are all valid

if __name__ == "__main__":
    unittest.main()
