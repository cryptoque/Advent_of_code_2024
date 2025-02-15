from sympy import Matrix

def parse_input():
    claw_input = []
    with open("input.txt", "r") as f:
        for idx, line in enumerate(f):
            e = line.strip().split(" ")
            if idx%4 == 0 or idx%4 == 1:
                claw_input.append([int(e[2].split("+")[1][:-1]), int(e[3].split("+")[1])])
            elif idx%4==2:
                claw_input.append([int(e[1].split("=")[1][:-1]), int(e[2].split("=")[1])])
    claw = list(zip(*(iter(claw_input),) * 3))
    return claw

def cost(claw, addition):
    # solve for:
    # m*A[0]+m*B[0] = goal[0]
    # n*A[1]+n*B[1] = goal[1]
    price = 0
    for machine in claw:
        p1, p2, goal = machine
        goal = [a + addition for a in goal]
        A = Matrix([[p1[0], p2[0]], [p1[1], p2[1]]])
        b = Matrix(goal)
        
        try:
            solution = A.solve(b)
            m, n = solution[0], solution[1]
            if m.is_integer and n.is_integer:
                price += m*3+n*1
        except ValueError:
            print("No solution found. The system may be singular or unsolvable.")
    return price

claw = parse_input()
print(cost(claw, 0))
print(cost(claw, 10000000000000))
                    
                
            
            
