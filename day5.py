import unittest

def parse_lines(file):
  pass

def get_overlapping(lines):
  pass

def overlapping_points(lines):
  pass

class TestDay5(unittest.TestCase):
    def test_part1(self):
      self.assertEqual(overlapping_points("data/testinput5.txt"), 5)
      print("Day 5, Part 1: ", overlapping_points("data/input5.txt"))

if __name__ == '__main__':
  unittest.main()
