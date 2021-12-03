with open("data/input1.txt") as f:
  lines = f.readlines()
  last_depth = None
  deeper = 0

  for line in lines:
    depth = int(line)

    if last_depth is None:
      last_depth = depth
      continue

    if depth > last_depth:
      deeper += 1

    last_depth = depth
  
  print(deeper)