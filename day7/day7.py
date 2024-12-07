import itertools, math

def parse_input():
    eqs = []
    with open("input.txt", "r") as file:
        parsed_input = [line.strip().split(":") for line in file]
    for item in parsed_input:
        eqs.append([int(item[0]), list(map(int, item[1].strip().split()))])
    return eqs

def operator_combination(num_operators, operator_types):
    #operators = ["+", "*", "||"]
    return list(itertools.product(operator_types, repeat=num_operators))

def cal_result(operator, right, left):
    result = right[0]
    for i in range(len(operator)):
        if result > left:
            return math.inf
        if operator[i] == "+":
            result += right[i+1]
        elif operator[i] == "*":
            result *= right[i+1]
        elif operator[i] == "||":
            # e.g. 14||93
            result = result*(10**len(str(right[i+1])))+right[i+1]
    return result

def valid_equation(left, right, operator_types):
    num_operators = len(right) -1

    ops = operator_combination(num_operators, operator_types)
    for op in ops:
        if left == cal_result(op, right, left):
            return True
    return False
            
def part1():
    sum = 0
    eqs = parse_input()
    for eq in eqs:
        if valid_equation(eq[0], eq[1], ["+", "*"]):
            sum+=eq[0]
    return sum

def part2():
    sum = 0
    eqs = parse_input()
    for eq in eqs:
        if valid_equation(eq[0], eq[1], ["+", "*", "||"]):
            sum+=eq[0]
    return sum

print(part1())
print(part2())
