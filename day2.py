def parse(line):
  command, magnitude = line.split(" ")
  magnitude = int(magnitude)
  return command, magnitude

def get_result():
  depth = 0
  position = 0

  with open("data/input2.txt") as f:
    lines = f.readlines()
    for line in lines:
      command, magnitude = parse(line)
      if command == "forward":
        position += magnitude
      elif command == "down":
        depth += magnitude
      elif command == "up":
        depth -= magnitude
    
    print(depth * position)

  return depth * position

if __name__ == "__main__":
  get_result()