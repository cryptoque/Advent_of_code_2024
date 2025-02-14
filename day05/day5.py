from collections import defaultdict, deque

def parse_input():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
        rules = [tuple(map(int, line.split("|"))) for line in lines[0].strip().split("\n")]
        updates = [list(map(int, line.split(","))) for line in lines[1].strip().split("\n")]
    return rules, updates

def build_graph(rules, update):
    graph = defaultdict(list)
    depth = defaultdict(int)
    for n1, n2 in rules:
        if n1 in update and n2 in update:
            graph[n1].append(n2)
            depth[n2] += 1
            depth[n1] += 0
    return graph, depth

def update_valid(graph, update):
    seen = set()
    for n in update:
        if any(x in seen for x in graph[n]):
            return False
        seen.add(n)
    return True

def sum_good_updates(updates, rules):
    sum_good = 0
    for update in updates:
        graph, _ = build_graph(rules, set(update))
        if update_valid(graph, update):
            sum_good += update[len(update)//2]
    return sum_good

def topological_sort(graph, depth):
    zero_depth = deque([node for node in depth if depth[node] == 0])
    sorted_update = []
    while zero_depth:
        node = zero_depth.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            depth[neighbor] -= 1
            if depth[neighbor] == 0:
                zero_depth.append(neighbor)
    return sorted_update

def sum_fixed_bad_updates(updates, rules):
    bad_updates = []
    for update in updates:
        graph, _ = build_graph(rules, set(update))
        if not update_valid(graph, update):
            bad_updates.append(update)
    sum_bad = 0
    for update in bad_updates:
        graph, depth = build_graph(rules, set(update))
        sorted_update = topological_sort(graph, depth)
        sum_bad += sorted_update[len(sorted_update)//2]
    return sum_bad
        

rules, updates = parse_input()
print(sum_good_updates(updates, rules))
print(sum_fixed_bad_updates(updates, rules))


