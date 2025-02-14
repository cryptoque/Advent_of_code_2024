from collections import defaultdict
import itertools


def parse_input():
    with open("input.txt", "r") as f:
        l = [line.strip().split("-") for line in f]
    return l

lans = parse_input()

lans1 = defaultdict(list)
for lan in lans:
    lans1[lan[0]].append(lan[1])
    lans1[lan[1]].append(lan[0])

computers = lans1.keys()

lans2 = set()
for k, v in lans1.items():
    for x in v:
        for y in lans1[x]:
            if y in v and (y.startswith("t") or k.startswith("t") or x.startswith("t")):
                lans2.add(tuple(sorted((k, x, y))))

print(len(lans2))
    
                
        
    
    
