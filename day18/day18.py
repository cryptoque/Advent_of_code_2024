
import numpy as np
import heapq


def parse_input():
    with open("input.txt", "r") as f:
        b = []
        for line in f:
            y, x = line.strip().split(",")
            b.append((int(x),int(y)))
    return b

def get_maze(b, r, c, n):
    maze = [["." for _ in range(c)] for _ in range(r)]
    for byte in b[:n]:
        maze[byte[0]][byte[1]] = "#"
    return maze

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
def a_algo_with_obstables(maze, start, end):
    r, c = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    open_set = []
    came_from = {}
    heapq.heappush(open_set, (0, 0, start[0], start[1], 0))
    g_score = {(start[0], start[1]): 0}
    visited = set()
    
    while open_set:
        _, current_g, x, y, pre_dir = heapq.heappop(open_set)
        if (x, y) == end:
            path = []
            while (x, y) in came_from:
                path.append((x, y))
                x, y = came_from[(x, y)]
            path.append(start)
            return current_g, path[::-1]
        
        if (x, y, pre_dir) in visited:
            continue
        visited.add((x, y, pre_dir))
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and maze[nx][ny] != "#":
                tentative_g = current_g + 1
                if (nx, ny) not in g_score or g_score[(nx, ny)] > tentative_g:
                    g_score[(nx, ny)] = tentative_g
                    f_score = tentative_g + heuristic((nx, ny), end)
                    heapq.heappush(open_set, (f_score, tentative_g, nx, ny, i))
                    came_from[(nx, ny)] = (x, y)

    return None, None
    
def find_shortest_path(bytes, r, c, n):
    maze = get_maze(bytes, r, c, n)
    sp = a_algo_with_obstables(maze, (0,0), (r-1,c-1))
    return sp[0]
    
def find_first_byte(bytes, r, c):
    maze = [["." for _ in range(r)] for _ in range(c)]
    for i in range(len(bytes)):
        for byte in bytes[:i]:
            maze[byte[0]][byte[1]] = "#"
        sp = a_algo_with_obstables(maze, (0,0), (r-1,c-1))
        if not sp[0]:
            return list(reversed(bytes[i-1]))

bytes = parse_input()
result1 = find_shortest_path(bytes, 71, 71, 1024)
print(result1)
result2 = find_first_byte(bytes, 71, 71)
print(result2)
