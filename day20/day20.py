import heapq

def parse_input():
    start = ()
    end = ()
    obstacles = []
    with open("input.txt", "r") as f:
        map = [list(line.strip()) for line in f]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start = (i, j)
            if map[i][j] == "E":
                end = (i, j)
            if start and end:
                break
    return map, start, end

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dijkstra_all_paths(maze, start, end):
    r, c = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start, [start])]
    g_score = {start: 0}
    all_paths = []
    shortest_dist = float('inf')
    while pq:
        current_dist, current, path = heapq.heappop(pq)
        if current_dist > shortest_dist:
            continue

        if current == end:
            shortest_dist = current_dist
            all_paths.append(path)
            continue

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != "#":
                tentative_g = current_dist + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    heapq.heappush(pq, (tentative_g, neighbor, path + [neighbor]))
                elif tentative_g == g_score[neighbor]:
                    heapq.heappush(pq, (tentative_g, neighbor, path + [neighbor]))

    return all_paths

def cheat(routes, cheat_sec):
    count = 0
    n = len(routes)
    for i in range(n):
        for j in range(i+100, n):
            point1, point2 = routes[i], routes[j]
            h = heuristic(point1, point2)
            if h<=cheat_sec and j-i-h>=100:
                count+= 1
    return count

map, start, end = parse_input()
routes = dijkstra_all_paths(map, start, end)[0]

# part 1
print(cheat(routes, 2))
# part 2
print(cheat(routes, 20))

    
    
