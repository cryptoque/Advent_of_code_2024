def parse_input():
    with open("input.txt", "r") as file:
        input_map = [list(line.strip()) for line in file]
    t_map = [list(map(int, line)) for line in input_map]
    return t_map

def find_nodes(t_map, target):
    target_nodes = []
    for i in range(len(t_map)):
        for j in range(len(t_map[0])):
            if t_map[i][j] == target: 
                target_nodes.append((i, j))
    return target_nodes

def within_boundary(x, y, r, c):
    if 0<=x<r and 0<=y<c:
        return True

def get_next_nodes(x, y, t_map):
    next_nodes = []
    r = len(t_map)
    c = len(t_map[0])
    next_value = t_map[x][y] + 1
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if within_boundary(nx, ny, r, c) and t_map[nx][ny] == next_value:
            next_nodes.append((nx, ny))
    return next_nodes

def search_path(x, y, t_map, seen):
    count = 0
    if t_map[x][y] == 9:
        if (x, y) not in seen:
            count += 1
            seen.add((x,y))
        else:
            pass
    else:
        next_nodes = get_next_nodes(x, y, t_map)
        for next_node in next_nodes:
            count += search_path(next_node[0], next_node[1], t_map, seen)
    return count

t_map = parse_input()
trailheads = find_nodes(t_map, 0)
score =  0
for (x, y) in trailheads:
    seen = set()
    score += search_path(x, y, t_map, set())
print(score)


