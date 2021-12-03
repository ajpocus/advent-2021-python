import unittest

def get_power(input_path):
  power = 0
  bit_histogram = None
  digit_count = 0

  with open(input_path) as f:
    lines = f.readlines()
    digit_count = len(lines[0]) - 1
    bit_histogram = []
    for _ in range(digit_count):
      bit_histogram.append([0, 0]) # needed to prevent shared memory that occurs with [] * n
    
    for pos in range(digit_count):
      for line in lines:
        bin_num = int("0b" + line, 2)
        bit_test = bin_num & (1 << (digit_count - pos - 1))
        bit = 0
        if bit_test > 0: bit = 1
        bit_histogram[pos][bit] += 1
    
    gamma = 0
    epsilon = 0

    for idx, pair in enumerate(bit_histogram):
      if pair[1] > pair[0]:
        gamma += (1 << (digit_count - idx - 1))

    epsilon = gamma ^ (2 ** digit_count - 1) # invert the bits
    power = gamma * epsilon

  return power

def get_bit_pattern(numbers, significand):
  keepers = numbers[:]
  offset = len(bin(numbers[0][2:])) - 1
  hgram = []

  for _ in range(offset + 1):
    hgram.append([0, 0]) # needed to prevent shared memory that occurs with [] * n
    
  while offset >= 0:
    nums = keepers[:]

    opp = significand ^ 1
    mcb = opp
    if hgram[offset][significand] >= hgram[offset][opp]:
      mcb = significand

    for num in nums:
      bit_test = num & (mcb << offset)
      if bit_test != 0:
        if len(keepers) == 1:
          return keepers[0]
        else:
          keepers.remove(num)
    
    offset -= 1

def get_life_suppport(input_path):
  with open(input_path) as f:
    lines = f.readlines()
    offset = len(lines[0]) - 1
    keepers = [int("0b" + line, 2) for line in lines]
    oxygen = 0
    co2 = 0

    for _ in range(offset + 1):
      hgram.append([0, 0]) # needed to prevent shared memory that occurs with [] * n

    for num in keepers:
      first_bit = num & (1 << offset)
      if first_bit == 0:
        hgram[offset][0] += 1
      else:
        hgram[offset][1] += 1

    nums = [int("0b" + line, 2) for line in lines]
    oxygen = get_bit_pattern(nums, 1)
    co2 = get_bit_pattern(nums, 0)

    return co2 * oxygen

class TestDay3(unittest.TestCase):

    def test_part1(self):
      self.assertEqual(get_power("data/testinput3.txt"), 198)
      print("POW", get_power("data/input3.txt"))

    def test_part2(self):
      self.assertEqual(get_life_suppport("data/testinput3.txt"), 230)
      print("LIFE", get_life_suppport("data/input3.txt"))

if __name__ == '__main__':
    unittest.main()