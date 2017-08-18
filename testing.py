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

    def test_sameInvalid1(self):
        self.assertFalse(word_ladder.same("hide", "the"))

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

    def test_buildInvalid1(self):
        words = ['aide', 'bide', 'down', 'hide', 'loan', 'side', 'seek']
        seen = {"the": True}
        list = []
        self.assertFalse(word_ladder.build(".he", words, seen, list))

# Previous functions make sure that the functions parameters are all valid for the following functions
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

    def test_findValid1(self):
        word = "lead"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        target = "gold"
        seen = {"lead": True}
        path = [word]
        depth = 4
        self.assertTrue(word_ladder.find(word, words, seen, target, path, depth))

    def test_findValid2(self):
        word = "lead"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        target = "gold"
        seen = {"lead": True}
        path = [word]
        depth = 2
        self.assertFalse(word_ladder.find(word, words, seen, target, path, depth))

    def test_findValid3(self):
        word = "hell"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        target = "gold"
        seen = {"hell": True}
        path = [word]
        depth = 4
        self.assertFalse(word_ladder.find(word, words, seen, target, path, depth))

    def test_IDDFSValid1(self):
        start = "lead"
        target = "gold"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        seen = {"lead": True}
        path = [start]
        min = len(start) - word_ladder.same(start, target)
        max = len(start) + min
        self.assertTrue(word_ladder.IDDFS(start, target, seen, words, path, min, max))

    def test_IDDFSValid2(self):
        start = "hell"
        target = "gold"
        words = ['coal', 'down', 'goad', 'sole', 'foal', 'load', 'loan', 'moan', 'seek']
        seen = {"hell": True}
        path = [start]
        min = len(start) - word_ladder.same(start, target)
        max = len(start) + min
        self.assertFalse(word_ladder.IDDFS(start, target, seen, words, path, min, max))

if __name__ == "__main__":
    unittest.main()
