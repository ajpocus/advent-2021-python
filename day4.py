import unittest
import numpy as np

def isblank(n):
  return n == "" or n == " " or n == "\n"

class Board:
  def __init__(self, raw_lines):
    lines = raw_lines[1:] 
    rows = [line.split(" ") for line in lines]
    rows = [[int(n) for n in row if not isblank(n)] for row in rows]
    self.rows = rows
    self.found = []

  def has_num(self, num):
    for row in self.rows:
      if num in row:
        self.found.append(num)
        return True

    return False

  def is_winner(self):
    for row in self.rows:
      if all(n in self.found for n in row):
        return True

    for idx in range(len(self.rows)):
      column = [row[idx] for row in self.rows]
      if all(n in self.found for n in column):
        return True

    return False

  def score(self):    
    unmarked_numbers = []
    for row in self.rows:
      for n in row:
        if n not in self.found:
          unmarked_numbers.append(n)

    last_num = self.found[-1]

    return sum(unmarked_numbers) * last_num

def get_winning_board(nums, boards):
  for num in nums:
    for board in boards:
      if board.has_num(num) and board.is_winner():
        return board

def score(filename):
  with open(filename) as f:
    lines = f.readlines()
    numline = lines[0]
    boardlines = lines[1:]
    nums = [int(n) for n in numline.split(",")]
    raw_boards = np.split(np.array(boardlines), 3)
    boards = [Board(b) for b in raw_boards]

    winning_board = get_winning_board(nums, boards)
    return winning_board.score()

class TestDay4(unittest.TestCase):
    def test_part1(self):
      self.assertEqual(score("data/testinput4.txt"), 4512)
      print("SCORE", score("data/input4.txt"))

if __name__ == '__main__':
  unittest.main()