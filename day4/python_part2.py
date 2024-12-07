import numpy as np

with open("input.txt", "r") as file:
    input_list = [list(line.strip()) for line in file]

s = np.array(input_list)

def search_xmas(i, j, s):
    r, c = s.shape
    count = 0
    # count mas, sam
    if i-1>=0 and j-1>=0 and i+1< r and j+1<c and s[i-1, j-1] == "M" and s[i+1, j-1] == "M" and s[i-1, j+1] == "S" and  s[i+1, j+1] == "S":
        count +=1
    # count sam, sam
    if i-1>=0 and j-1>=0 and i+1< r and j+1<c and s[i-1, j-1] == "S" and s[i+1, j-1] == "M" and s[i-1, j+1] == "S" and  s[i+1, j+1] == "M":
        count +=1
    # count sam, mas
    if i-1>=0 and j-1>=0 and i+1< r and j+1<c and s[i-1, j-1] == "S" and s[i+1, j-1] == "S" and s[i-1, j+1] == "M" and  s[i+1, j+1] == "M":
        count +=1
    # count mas, mas
    if i-1>=0 and j-1>=0 and i+1< r and j+1<c and s[i-1, j-1] == "M" and s[i+1, j-1] == "S" and s[i-1, j+1] == "M" and  s[i+1, j+1] == "S":
        count +=1
    return count

count = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i, j] == "A":
            count += search_xmas(i, j, s)
print(count)




