import numpy as np
import heapq

def parse_input():
    with open("input.txt", "r") as f:
        maze = [list(line.strip()) for line in f]
        for idx, x in enumerate(maze):
            for idy, y in enumerate(x):
                if "S" in y:
                    start = (idx, idy)
                if "E" in y:
                    end = (idx, idy)
        
    return maze, start, end


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
                turn_penalty = 1000 if pre_dir != i else 0
                tentative_g = current_g + 1 + turn_penalty
                if (nx, ny) not in g_score or g_score[(nx, ny)] > tentative_g:
                    g_score[(nx, ny)] = tentative_g
                    f_score = tentative_g + heuristic((nx, ny), end)
                    heapq.heappush(open_set, (f_score, tentative_g, nx, ny, i))
                    came_from[(nx, ny)] = (x, y)

    return None, None
    

        
    
maze, start, end = parse_input()
print(maze)
sp = a_algo_with_obstables(maze, start, end)
print(sp)


        
