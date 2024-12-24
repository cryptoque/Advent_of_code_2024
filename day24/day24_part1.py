def parse_input():
    inputs = {}
    eq = {}
    with open("input.txt", "r") as f:
        x, y = f.read().split("\n\n")
        x = x.split("\n")
        for e in x:
            x1 = e.split(": ")
            inputs[x1[0]] = int(x1[1])
        y = y.split("\n")
        for e in y:
            left, right = e.split(" -> ")
            x1, op, x2 = tuple(left.split(" "))
            eq[right] = {op: (x1, x2)}
    return inputs, eq
    
    
inputs, eqs = parse_input()

def op(operator, x, y):
    if operator == "XOR":
        return x^y
    elif operator == "AND":
        return x and y
    elif operator == "OR":
        return x or y

def apply_op(eq, inputs, target):
    r = eq[target]
    #print(list(r.keys()))
    #print(list(r.values())[0][0],list(r.values())[0][1])
    operator, x, y = list(r.keys())[0], list(r.values())[0][0], list(r.values())[0][1]
    if (x.startswith("x") or x.startswith("y")) and (y.startswith("x") or y.startswith("y")):
        x = inputs[x]
        y = inputs[y]
    elif (x.startswith("x") or x.startswith("y")):
        x = inputs[x]
        y = apply_op(eq, inputs, y)
    elif (y.startswith("x") or y.startswith("y")):
        y = inputs[y]
        x = apply_op(eq, inputs, x)
    else:
        x = apply_op(eq, inputs, x)
        y = apply_op(eq, inputs, y)
    return op(operator, x, y)

out = {}
for k, v in eqs.items():
    if k.startswith("z"):
        out[k] = apply_op(eqs, inputs, k)

result1 = ""
d = dict(sorted(out.items(), key=lambda item: item[0], reverse=True))
print(d)
for e in d.values():
    result1+=str(e)
print(int(result1, 2))
