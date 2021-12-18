import unittest
import numpy as np

def isblank(n):
  return n == "" or n == " " or n == "\n"

# Code modified from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
# Licensed under CC-BY-SA 4.0
def chunks(lst, n):
    """Return n-sized chunks from lst."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

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

  def get_score(self):
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

def filter_funk(item):
  return item is not None and item.is_winner()

def get_losing_board(nums, boards):
  remainders = boards[:]
  for num in nums:
    if len(remainders) == 1:
      return remainders.pop()

    for idx, board in enumerate(boards):
      if board is not None and board.has_num(num) and board.is_winner():
        remainders[idx] = None

def score(filename):
  with open(filename) as f:
    lines = f.readlines()
    numline = lines[0]
    boardlines = lines[1:]
    nums = [int(n) for n in numline.split(",")]
    raw_boards = chunks(boardlines, 6)
    boards = [Board(b) for b in raw_boards]

    winning_board = get_winning_board(nums, boards)
    return winning_board.get_score()

def unscore(filename):
  with open(filename) as f:
    lines = f.readlines()
    numline = lines[0]
    boardlines = lines[1:]
    nums = [int(n) for n in numline.split(",")]
    raw_boards = chunks(boardlines, 6)
    boards = [Board(b) for b in raw_boards]

    losing_board = get_losing_board(nums, boards)
    return losing_board.get_score()

class TestDay4(unittest.TestCase):
    def test_part1(self):
      # self.assertEqual(score("data/testinput4.txt"), 4512)
      print("SCORE", score("data/input4.txt"))

    def test_part2(self):
      self.assertEqual(unscore("data/testinput4.txt"), 1924)
      print("SCORE LOSER", unscore("data/input4.txt"))
if __name__ == '__main__':
  unittest.main()
