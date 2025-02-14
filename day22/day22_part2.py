from collections import defaultdict
import itertools

def parse_input():
    with open("input.txt", "r") as f:
        buyers = [int(line.strip()) for line in f]
    return buyers

def mix(v, secret):
    return v^secret
def prune(secret):
    return secret % 16777216

def next_secret(secret):
    v = secret * 64
    secret = prune(mix(v, secret))
    v = secret // 32
    secret = prune(mix(v, secret))
    v = secret * 2048
    return prune(mix(v, secret))

prices = []
buyers = parse_input()
for buyer in buyers:
    price = []
    for i in range(2000):
        buyer = next_secret(buyer)
        price.append(buyer)
    prices.append(price)

result1 = 0
for price in prices:
    result1+= price[-1]

print(result1)

changes = []
for i, price in enumerate(prices):
    change = []
    for a, b in itertools.pairwise(price):
        change.append(b%10-a%10)
    changes.append(change)

all_seqs = []
for i, change in enumerate(changes):
    seq = {}
    for j in range(len(change)-4):
        seq[(change[j], change[j+1], change[j+2], change[j+3])] = prices[i][j+4]%10
    all_seqs.append(seq)
print("finished buiding patterns")

unique_patterns = set()
for seq in all_seqs:
    unique_patterns |= seq.keys()
    
print("found all unique patterns")

print(len(unique_patterns))
max_banana = 0
for p in unique_patterns:
    bananas = 0
    for seq in all_seqs:
        if p in seq:
            bananas+=seq[p]
    if bananas>max_banana:
        max_banana = bananas

print(max_banana)
