from collections import defaultdict
import numpy as np

def parse_input():
    robots = []
    with open("input.txt", "r") as file:
        for r in file:
            robot = []
            pv = r.strip().split(" ")
            robot.append(list(map(int, pv[0][2:].split(","))))
            robot.append(list(map(int, pv[1][2:].split(","))))
            robots.append(robot)
    robots = np.array(robots)
    return robots

def seconds(t, robots, a, b):
    map = defaultdict(int)
    for idx, robot in enumerate(robots):
        vt = (robot[1] * t)
        new_loc = robot[0] + vt
        map[idx] =[int(new_loc[0]%a), int(new_loc[1]%b)]
    return map

def count_quadrant(map, a, b):
    l = [[(0, a//2),(0, b//2)], [(a//2+1, a), (b//2+1, b)], [(0, a//2), (b//2+1, b)], [(a//2+1, a), (0, b//2)]]
    cq = {0: 0, 1: 0, 2: 0, 3:0}
    for _, v in map.items():
        for idx, q in enumerate(l):
            if v[0] in range(*q[0]) and v[1] in range(*q[1]):
                cq[idx] +=1
    return cq
                
def draw(map, a, b):
    grid = [[' ' for _ in range(a)] for _ in range(b)]
    for _, v in map.items():
        grid[v[1]][v[0]] = "+"
    for row in grid:
        print("".join(row))
            
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    return True
  

robots = parse_input()
map = seconds(100, robots, 101, 103)
cq = count_quadrant(map, 101, 103)
p = 1
for _, v in cq.items():
    p*=v

# part one solution
print(p)

# print the output into a file ~60 outputs and identify the tree from there.
for i in range(0, 10000):
    map = seconds(i, robots, 101, 103)
    cq = count_quadrant(map, 101, 103)
    for _,v in cq.items():
        if v>=200:
            print(i)
            draw(map, 101, 103)

            
        
    
    
    


