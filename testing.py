import word_ladder
import unittest

file = open("dictionary.txt")
lines = file.readlines()

list = []
words = []
start = "goal"
seen = {start: True}
target = "play"
for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
        words.append(word)


class TestLaddergram(unittest.TestCase):

    def test_sameValidIn1(self):
        self.assertEqual(word_ladder.same("the", "say"), 0)

    def test_sameValidIn2(self):
        self.assertEqual(word_ladder.same("goal", "load"), 2)

    def test_sameInvalidIn1(self):
        self.assertEqual(word_ladder.same("goal", "led"), 0)

    def test_sameInvalidIn2(self):
        self.assertEqual(word_ladder.same("goal", ""), 0)

    def test_sameInvalidIn3(self):
        self.assertFalse(word_ladder.same("goal", 123))

    def test_buildValidIn(self):
        self.assertEqual(word_ladder.build(".oal", words, seen, list), ['coal', 'foal'])

    def test_buildValidIn2(self):
        self.assertEqual(word_ladder.build(".ide", words, seen, list), ['aide', 'bide', 'eide', 'hide', 'nide', 'ride', 'side', 'tide', 'vide', 'wide'])

    def test_buildInvalidIn(self):
        self.assertFalse(word_ladder.build([], words, seen, list))

    def test_buildInvalidIn2(self):
        self.assertFalse(word_ladder.build(1, words, seen, list))

    def test_buildInvalidIn3(self):
        self.assertFalse(word_ladder.build("", words, seen, list))

    def test_buildInvalidIn4(self):
        self.assertFalse(word_ladder.build(".ide", [], seen, list))

    def test_buildInvalidIn5(self):
        self.assertFalse(word_ladder.build(".ide", words, {}, list))

if __name__ == "__main__":
    unittest.main()