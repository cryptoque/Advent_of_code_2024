import math
import itertools
from collections import defaultdict
from fractions import Fraction

def get_antinode_loc_part1(antenna_pair_loc, bound_x, bound_y):
    (x1, y1), (x2, y2) = antenna_pair_loc
    dx, dy = x2 - x1, y2 - y1
    return [ (x, y) for x, y in [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)] if 0 <= x < bound_x and 0 <= y < bound_y ]

def get_antinode_loc_part2(antenna_pair_loc, bound_x, bound_y):
    # (2,3), (-4,7)
    antinodes = []
    (x1, y1), (x2, y2) = antenna_pair_loc
    dx, dy = x2-x1, y2-y1
    if dx == 0: #vertical
        for y in range(bound_y):
            antinodes.append((x1, y))
    elif dy == 0: #horizontal
        for x in range(bound_x):
            antinodes.append((x, y1))
    else:
        k = Fraction(dy, dx)
        b = y1 - x1*k
        # y = k*x+b
        for x in range(bound_x):
            y = k*x+b
            if 0 <= y <bound_y and y.denominator == 1:
                antinodes.append((x,y))
    return antinodes


def select_two_combination(l):
    return list(itertools.combinations(l, 2))

def digest_map(map_input):
    d = defaultdict(list)
    for i in range(len(map_input)):
        for j in range(len(map_input[i])):
            if map_input[i][j].isalnum():
                d[map_input[i][j]].append((i, j))
    return d


with open("input.txt", "r") as file:
    map_input = [list(line.strip().split()[0]) for line in file]
d = digest_map(map_input)

boundary_x = len(map_input)
boundary_y = len(map_input[0])
antinodes_part1 = set()
antinodes_part2 = set()

for _, v in d.items():
    antenna_pair_locs = select_two_combination(v)
    for antenna_pair_loc in antenna_pair_locs:
        antinodes1 = get_antinode_loc_part1(antenna_pair_loc, boundary_x, boundary_y)
        antinodes2 = get_antinode_loc_part2(antenna_pair_loc, boundary_x, boundary_y)
        for antinode in antinodes1:
            antinodes_part1.add(antinode)
        for antinode in antinodes2:
            antinodes_part2.add(antinode)

count1 = len(antinodes_part1)
count2 = len(antinodes_part2)
    
print(count1)
print(count2)
    
