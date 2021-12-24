import unittest

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def is_vertical(self):
        return self.y1 == self.y2

    def is_horizontal(self):
        return self.x1 == self.x2

    def overlaps(self, other):
        if self.is_horizontal():
            return not other.is_horizontal() and self.y1 > other.y1 and self.y2 < other.y2
        elif self.is_vertical():
            return not other.is_vertical() and self.x1 > other.x1 and self.x2 > other.x2
        else:
            return False

def get_raw_lines(filename):
    with open(filename) as f:
        return f.readlines()

def parse_lines(raw_lines):
    matches = []
    for raw_line in raw_lines:
        coord1, coord2 = raw_line.split(" -> ")
        x1, y1 = [int(n) for n in coord1.split(",")]
        x2, y2 = [int(n) for n in coord2.split(",")]
        if x1 == x2 or y1 == y2: # line is vertical or horizontal
            matches.append(Line(x1, y1, x2, y2))

    return matches

def get_overlapping(lines):
    overlapping_lines = []

    for line_idx, line in enumerate(lines):
        for other_idx, other_line in enumerate(lines):
            if line_idx == other_idx:
                continue
            
            if line.overlaps(other_line) and line not in overlapping_lines:
                overlapping_lines.append(line)

    return overlapping_lines

def draw_lines(lines):
    max_value = 1
    for line in lines:
        if line.x1 > max_value or line.y1 > max_value or line.x2 > max_value or line.y2 > max_value:
            max_value = max(line.x1, line.y1, line.x2, line.y2)

    grid = []
    for _ in range(max_value + 1):
        row = []
        for _ in range(max_value + 1):
            row.append(0)
        
        grid.append(row)
    
    for line in lines:
        if line.is_horizontal():
            y = line.y1
            for x in range(line.x1, line.x2 + 1):
                grid[x][y] += 1
        else:
            x = line.x1
            for y in range(line.y1, line.y2 + 1):
                grid[x][y] += 1

    return grid

def overlapping_points(filename):
    raw_lines = get_raw_lines(filename)
    lines = parse_lines(raw_lines)
    overlapping_lines = get_overlapping(lines)
    grid = draw_lines(overlapping_lines)
    points = 0

    for row in grid:
        for square in row:
            if square > 1:
                points += 1

    return points

class TestDay5(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(overlapping_points("data/testinput5.txt"), 5)
        print("Day 5, Part 1: ", overlapping_points("data/input5.txt"))

if __name__ == '__main__':
    unittest.main()
