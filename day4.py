import unittest

def get_score(filename):
  pass

class TestDay4(unittest.TestCase):
    def test_part1(self):
      self.assertEqual(get_score("data/testinput4.txt"), 4512)
      print("SCORE", get_score("data/input4.txt"))

if __name__ == '__main__':
  unittest.main()