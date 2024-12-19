from collections import defaultdict

def parse_input():
    with open("input.txt", "r") as f:
        r, p= f.read().split("\n\n")
    r = r.split("\n")
    registers = defaultdict(int)
    for register in r:
        n, v = register.split(":")
        n = n.split(" ")[1]
        registers[n] = int(v)
    instructions = list(map(int, p.split(" ")[1].split(",")))
    return registers, instructions

def combo_operand(instr, reg):
    if 0<=instr <=3:
        return instr
    elif instr == 4:
        return reg["A"]
    elif instr == 5:
        return reg["B"]
    elif instr == 6:
        return reg["C"]
    else:
        return None

def execute(reg, opcode, oprand, output):
    match opcode:
        case 0:
            r = reg["A"]/2**combo_operand(oprand, reg)
            reg["A"] = int(r)
        case 1:
            reg["B"] = reg["B"] ^ oprand
        case 2:
            reg["B"] = combo_operand(oprand, reg) % 8
        case 3:
            pass # handled specifically
        case 4:
            reg["B"] = reg["B"] ^ reg["C"]
        case 5:
            output.append(combo_operand(oprand, reg) % 8)
        case 6:
            r = reg["A"]/2**combo_operand(oprand, reg)
            reg["B"] = int(r)
        case 7:
            r = reg["A"]/2**combo_operand(oprand, reg)
            reg["C"] = int(r)
        

reg, instructions = parse_input()
output = []
pointer = 0
end = len(instructions)-2
while(pointer<=end):
    if instructions[pointer] == 3 and reg["A"] !=0:
        pointer = instructions[pointer+1]
    else:
        execute(reg, instructions[pointer], instructions[pointer+1], output)
        pointer+=2

print(",".join(map(str, output)))
