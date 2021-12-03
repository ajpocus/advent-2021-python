WINDOW_SIZE = 3

def window(lines, start):
  if start > len(lines) - WINDOW_SIZE:
    return None
  
  return int(lines[start]), int(lines[start+1]), int(lines[start+2])

with open("data/input1.txt") as f:
  lines = f.readlines()
  end_idx = len(lines) - WINDOW_SIZE + 1
  last_sum = None
  larger_count = 0

  for i in range(0, end_idx):
    nums = window(lines, i)
    this_sum = sum(nums)
    if last_sum is None:
      last_sum = this_sum
      continue

    if this_sum > last_sum:
      larger_count += 1
    
    last_sum = this_sum

  print(larger_count)