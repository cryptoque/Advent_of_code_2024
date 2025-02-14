from collections import defaultdict
def parse_input():
    with open("input.txt", "r") as f:
        map, moves = f.read().split("\n\n")
    map = [list(s) for s in map.split("\n")]
    r = len(map)
    c = len(map[0])
    
    robot_loc = ()
    walls = defaultdict(bool)
    boxes = defaultdict(bool)
    
    for idx, v1 in enumerate(map):
        for idy, v2 in enumerate(list(v1)):
            if map[idx][idy] == "@":
                robot_loc = (idx, idy)
            elif map[idx][idy] == "O":
                boxes[(idx, idy)] = True
            elif map[idx][idy] == "#":
                walls[(idx, idy)] = True
    return robot_loc, walls, boxes, moves, r, c


def handle_boxes(x, y, walls, boxes, dx, dy, r, c):
    if dx != 0:
        for i in range(1, r):
            if boxes[(x + i*dx, y + dy)]:
                #print("box again")
                continue
            elif walls[(x + i*dx, y + dy)]:
                #print("hit wall, return to: ", (x,y))
                return (x, y)
            else: #push boxes
                #print("pushing boxes ")
                #print("updated to true: ", (x+i*dx, y+dy))
                #print("updated to false: ", (x+dx, y+dy))
                boxes[(x+i*dx, y+dy)] = True
                boxes[(x+dx, y+dy)] = False
                return (x+dx, y+dy)

    elif dy!=0:
        for i in range(1, c):
            if boxes[(x + dx, y + i*dy)]:
                continue
            elif walls[(x + dx, y + i*dy)]:
                return (x, y)
            else:#push boxes
                #print("pushing boxes ")
                #print("updated to true: ", (x+dx, y+i*dy))
                #print("updated to false: ", (x+dx, y+dy))
                #print((x+dx, y+dy))
                boxes[(x+dx, y+i*dy)] = True
                boxes[(x+dx, y+dy)] = False
                return (x+dx, y+dy)



def go(robot_loc, walls, boxes, moves, r, c):
    d = {">": [0, 1], "<": [0, -1] , "^": [-1, 0], "v": [1, 0]}
    for move in moves:
        if move == "\n":
            continue
        #print(robot_loc)
        #print(move)
        #print(boxes)
        dx, dy = d[move]
        x = robot_loc[0]
        y = robot_loc[1]
        if walls[(x+dx,y+dy)]:
                continue
        elif boxes[(x+dx, y+dy)]:
            robot_loc = handle_boxes(x, y, walls, boxes, dx, dy,r, c)
        else:
            robot_loc = (x+dx, y+dy)
    return robot_loc
        
            
        
    
    
robot_loc, walls, boxes, moves, r, c = parse_input()
#print(robot_loc)
#print(walls)
#print(boxes)
#print(moves)

destination = go(robot_loc, walls, boxes, moves, r, c)
sum = 0
for k, v in boxes.items():
    if v:
        sum += k[0]*100+k[1]
    
print(sum)
