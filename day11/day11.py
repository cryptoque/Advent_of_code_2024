import time
from collections import Counter
def parse_input():
    with open("input.txt", "r") as file:
        stones = Counter([int(s) for s in file.read().strip().split()])
    return stones

def blink(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        value_s = str(stone)
        l = len(value_s)
        if stone == 0:
            new_stones[1] += count
        elif l%2 == 0:
            new_stones[int(value_s[:l//2])] += count
            new_stones[int(value_s[l//2:])] += count
        else:
            new_stones[stone*2024] += count
    return new_stones
        
stones = parse_input()

x = 0
while(x<25):
    stones = blink(stones)
    x+=1
print(sum(stones.values()))

while(x<75):
    stones = blink(stones)
    x+=1
print(sum(stones.values()))


