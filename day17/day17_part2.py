from z3 import *

target = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]
a = BitVec("a", 48)
b = 0
c = 0
temp_a = a
solver = Optimize()
for t in target:
    b = temp_a % 8
    b = b ^ 5
    c = temp_a>>b
    b = b ^ 6
    temp_a = temp_a>>3
    b = b ^ c
    solver.add((b%8)==t)
solver.add(temp_a==0)
solver.minimize(a)

if solver.check() == sat:
    model = solver.model()
    print(model[a].as_long())
    
