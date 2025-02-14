import numpy as np

def parse_input():
    locks = []
    keys = []
    with open("input.txt", "r") as f:
        lock_or_key = f.read().split("\n\n")
    for x in lock_or_key:
        t = x.split("\n")
        if t[0] == "#####":
            locks.append(list(map(list, t[1:-1])))
        else:
            keys.append(list(map(list, t[1:-1])))
    return locks, keys
    
def get_heights(lock_or_key):
    l = len(lock_or_key[0])
    m = np.array(lock_or_key)
    heights = []
    for i in range(l):
        heights.append(sum(1 for e in m[:,i] if e == "#"))
    return heights
    


locks, keys = parse_input()
heights_locks = []
heights_keys = []
for lock in locks:
    heights_locks.append(get_heights(lock))
for key in keys:
    heights_keys.append(get_heights(key))

matches = 0
for hk in heights_keys:
    for hl in heights_locks:
        if all(a+b<=5 for a, b in zip(hk, hl)):
            matches+=1
            
            
print(matches)

