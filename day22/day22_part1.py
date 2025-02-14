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
    
    
tth = []
buyers = parse_input()
prices = {}
for buyer in buyers:
    for i in range(2000):
        #print(i, buyer)
        buyer = next_secret(buyer)
    tth.append(buyer)
print(sum(tth))
