import heapq
from itertools import product
from collections import defaultdict, deque

def parse_input():
    with open("input.txt", "r") as f:
        codes = [list(line.strip()) for line in f]
    numbers = [["7","8","9"], ["4","5","6"], ["1","2","3"], ["#", "0", "A"]]
    directions = [["#", "^", "A"], ["<", "v", ">"]]
    return codes, numbers, directions


def create_keypad(layout):
    keypad = {}
    for y, row in enumerate(layout):
        for x, button in enumerate(row):
            if button == '#':
                continue
            neighbors = {}
            for dx, dy, move in [(-1, 0, '<'), (1, 0, '>'), (0, -1, '^'), (0, 1, 'v')]:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(layout) and 0 <= nx < len(layout[ny]) and layout[ny][nx] != '#':
                    neighbors[move] = layout[ny][nx]
            keypad[button] = neighbors
    return keypad

def bfs_all_shortest_paths(keypad, start, target):
    queue = deque([(start, "")])
    shortest_paths = []
    visited = {}
    min_length = float('inf')

    while queue:
        current, path = queue.popleft()

        if len(path) > min_length:
            continue

        if current == target:
            if len(path) < min_length:
                min_length = len(path)
                shortest_paths = [path]
            elif len(path) == min_length:
                shortest_paths.append(path)
            continue

        if current in visited and len(path) > visited[current]:
            continue

        visited[current] = len(path)

        for move, neighbor in keypad[current].items():
            queue.append((neighbor, path + move))

    return shortest_paths

def consolidate_combinations(sequences, paths):
    if not sequences or not paths:
        return paths
    return [seq + path for seq, path in product(sequences, paths)]

def robot_2_numbers(numbers_keypad, code):
    start = "A"
    sequences = []
    for digit in code:
        paths = bfs_all_shortest_paths(numbers_keypad, start, digit)
        for i in range(len(paths)):
            paths[i] += "A"
        sequences = consolidate_combinations(sequences, paths)
        start = digit
    return sequences

def robot_2_robots(robot_keypad, sequences):
    robot_sequences = []
    for sequence in sequences:
        new_sequences = robot_2_numbers(robot_keypad, sequence)
        if new_sequences:
            robot_sequences += new_sequences
        else:
            robot_sequences += "A"
    return robot_sequences


def get_v(code):
    return int("".join(code[:-1]))


codes, numbers, directions = parse_input()
numbers_keypad = create_keypad(numbers)
robot_keypad = create_keypad(directions)



result1 = 0
for code in codes:
    sequences = robot_2_numbers(numbers_keypad, code)
    robot_sequences1 = robot_2_robots(robot_keypad, sequences)
    min_length1 = min(len(s) for s in robot_sequences1)
    robot_sequences1 = [s for s in robot_sequences1 if len(s) == min_length1]
    
    robot_sequences2 = robot_2_robots(robot_keypad, robot_sequences1)
    min_length2 = min(len(s) for s in robot_sequences2)
    robot_sequences2 = [s for s in robot_sequences2 if len(s) == min_length2]
    print(get_v(code), len(robot_sequences2[0]))
    result1 += get_v(code) * len(robot_sequences2[0])
print(result1)



