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

def get_frequencies(nums):
  longest = max(len(bin(n)[2:]) for n in nums)
  hgram = []

  for _ in range(longest):
    hgram.append({ 0: 0, 1: 0 }) # needed to prevent shared memory that occurs with [] * n
  
  for shift in range(longest):
    for num in nums:
      bit_test = (num & (1 << shift))
      bit = 0
      if bit_test > 0: bit = 1
      hgram[shift][bit] += 1

  return hgram

def get_bit_pattern(numbers, most_popular):
  keepers = numbers[:]
  longest = max(len(bin(n)[2:]) for n in numbers)
  offset = longest - 1

  print("OFF", offset)

  hgram = get_frequencies(keepers)

  while offset >= 0:
    print("OFFSET", offset)
    print("KEEPERS", keepers)

    nums = keepers[:]

    if len(nums) == 2:
      pass

    bit = None
    print("OFF", offset)
    if hgram[offset][0] == hgram[offset][1]:
      if most_popular:
        bit = 1
      else:
        bit = 0
    else:
      if most_popular:
        bit = max(hgram[offset], key=hgram[offset].get)
      else:
        bit = min(hgram[offset], key=hgram[offset].get)

    for num in nums:
      test = False
      if bit == 0:
        test = ((num & (1 << offset)) == 0)
      else:
        test = ((num & (1 << offset)) > 0)

      if not test:
        keepers.remove(num)
        if len(keepers) == 1:
          return keepers[0]
    
    hgram = get_frequencies(keepers)
    offset -= 1
  
  return keepers[0]

def get_life_suppport(input_path):
  with open(input_path) as f:
    lines = f.readlines()
    nums = [int("0b" + line, 2) for line in lines]
    oxygen = get_bit_pattern(nums[:], True)
    co2 = get_bit_pattern(nums[:], False)

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