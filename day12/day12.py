import numpy as np
from collections import defaultdict
from collections import Counter

def parse_input():
    with open("input.txt", "r") as file:
        data = [list(line) for line in file.read().split()]
    plots = np.array(data, dtype=str)
    return plots

def flood_fill_recursive(plots, r, c, target, visited):
    rows, cols = plots.shape
    if r<0 or r>=rows or c<0 or c>=cols or visited[r, c] or plots[r, c] != target:
        return []
    visited[r, c] = True
    region = [(r, c)]
    region += flood_fill_recursive(plots, r+1, c, target, visited)
    region += flood_fill_recursive(plots, r-1, c, target, visited)
    region += flood_fill_recursive(plots, r, c+1, target, visited)
    region += flood_fill_recursive(plots, r, c-1, target, visited)
    return region

def get_perimeter(region):
    region_set = set(region)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    exposed = 0
    
    for x,y in region:
        for dx, dy in directions:
            if (x+dx, y+dy) not in region_set:
                exposed += 1
    return exposed
    
def get_regions(plots):
    rows, cols = plots.shape
    price = 0
    visited = defaultdict(bool)
    for idx, target in np.ndenumerate(plots):
        if not visited[idx]:
            region = flood_fill_recursive(plots, idx[0], idx[1], target, visited)
            area = len(region)
            perimeter = get_perimeter(region)
            price += area * perimeter
    return price

plots = parse_input()
result = get_regions(plots)
print(result)

