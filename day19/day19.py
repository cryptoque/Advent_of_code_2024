from collections import defaultdict

def parse_input():
    with open("input.txt", "r") as f:
        patterns, designs = f.read().split("\n\n")
    ps = patterns.strip().split(", ")
    ds = designs.strip().split("\n")
    return ps, ds

def is_possible(design, patterns):
    candidates = []
    if design == "":
        return 1
    for p in patterns:
        if design.startswith(p):
            candidates.append(p)
    if candidates == []:
        return 0
    return any(is_possible(design[len(c):], patterns) for c in candidates)
        

def count_ways(design, patterns, ways, store):
    if design in store.keys():
        return store[design]
    candidates = []
    if design == "":
        ways += 1
        return ways
    for p in patterns:
        if design.startswith(p):
            candidates.append(p)
    if candidates == []:
        store[design] = 0
        return 0
    store[design] = sum(count_ways(design[len(c):], patterns, ways, store) for c in candidates)
    return store[design]


ps, ds = parse_input()
s1 = 0
s2 = 0
store = defaultdict(int)
for d in ds:
    s1 += is_possible(d, ps)
    s2 += count_ways(d, ps, 0, store)
    
print(s1)
print(s2)
