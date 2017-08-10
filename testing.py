import word_ladder
import unittest

class TestLaddergram(unittest.TestCase):

    def test_getDictValid1(self):
        # The file dict.txt contains the words "a few words" separated by new lines
        self.assertEqual(word_ladder.getDict("dict.txt"), ["a\n", "few\n", "words"])

    def test_getDictInvalid1(self):
        # The file dict2.txt is empty
        self.assertFalse(word_ladder.getDict("dict2.txt"))

    def test_getDictInvalid2(self):
        self.assertFalse(word_ladder.getDict("blah"))

    def test_sameValid1(self):
        self.assertEqual(word_ladder.same("the", "say"), 0)

    def test_sameValid2(self):
        self.assertEqual(word_ladder.same("goal", "load"), 2)

    def test_sameInvalid1(self):
        self.assertFalse(word_ladder.same("goal", "goa"))

    def test_sameInvalid2(self):
        self.assertFalse(word_ladder.same("goal", ""))

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
        words = ['ate', 'bay', 'day', 'eat', 'map', 'the']
        seen = {'tea': True}
        list = []
        self.assertFalse(word_ladder.build("", words, seen, list))

    def test_buildInvalid2(self):
        words = []
        seen = {'tea': True}
        list = []
        self.assertFalse(word_ladder.build("tea", words, seen, list))

    def test_buildInvalid3(self):
        words = ['ate', 'bay', 'day', 'eat', 'map', 'the']
        seen = {'tea': True}
        list = []
        self.assertFalse(word_ladder.build(1, words, seen, list))

    def test_buildInvalid4(self):
        words = ['aide', 'bide', 'down', 'hide', 'loan', 'side', 'seek']
        seen = {}
        list = []
        self.assertFalse(word_ladder.build(".ide", words, seen, list))

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

    def test_shortestFindInvalid1(self):
        word = ""
        words = ['aide', 'bide', 'down', 'hide', 'loan', 'side', 'seek']
        target = "sees"
        seen = {"": True}
        self.assertFalse(word_ladder.shortestFind(word, words, target, seen))

    def test_shortestFindInvalid2(self):
        word = "side"
        words = ['aide', 'bide', 'down', 'hide', 'loan', 'side', 'seek']
        target = ""
        seen = {"": True}
        self.assertFalse(word_ladder.shortestFind(word, words, target, seen))

if __name__ == "__main__":
    unittest.main()