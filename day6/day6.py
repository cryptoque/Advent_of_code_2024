
def read_input():
    with open("input.txt", "r") as file:
        m = [list(line.strip()) for line in file]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "^":
                return m, i, j

def execute_route(m, i, j):
    r = len(m)
    c = len(m[0])
    
    direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    current_direction = 0
    visited = set()
    visited.add((i, j))

    while(0<i<r-1 and 0<j<c-1):
        dx, dy = direction[current_direction]
        while(m[i+dx][j+dy]=="#"):
            current_direction = (current_direction+1)%4
            dx, dy = direction[current_direction]
        i+=dx
        j+=dy
        visited.add((i, j))
    return visited

def is_loop(m, i, j):
    r = len(m)
    c = len(m[0])
    
    direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    current_direction = 0
    visited = set()
    visited.add((current_direction, i, j))

    while(0<i<r-1 and 0<j<c-1):
        dx, dy = direction[current_direction]
        while(m[i+dx][j+dy]=="#"):
            current_direction = (current_direction+1)%4
            dx, dy = direction[current_direction]
        i+=dx
        j+=dy
        if (current_direction, i, j) not in visited:
            visited.add((current_direction, i, j))
        else:
            return 1
    return 0

def part1():
    map_input, i, j = read_input()
    visited = execute_route(map_input, i, j)
    return len(visited)

def part2():
    loop = 0
    map, i, j = read_input()
    for x in range(len(map)):
        for y in range(len(map[0])):
            # place obstacle at (x, y)
            if map[x][y]!= "#" and map[x][y] !="^":
                map[x][y] = "#"
                loop += is_loop(map, i, j)
                map[x][y] = "."
    return loop

print(part1())
print(part2())
    
    
