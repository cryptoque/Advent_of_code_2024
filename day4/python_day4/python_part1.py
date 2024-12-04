import numpy as np

with open("input.txt", "r") as file:
    input_list = [list(line.strip()) for line in file]

s = np.array(input_list)

def search_xmas(i, j, s):
    r, c = s.shape
    count = 0
    # horizonal_forward
    if ((j+4) <= c) and ''.join(s[i,j+1:j+4]) == "MAS":    
        count += 1
    # horizontal_backward
    if ((j-3) >= 0) and ''.join(s[i, j-3:j]) == "SAM":
        count += 1
    # vertical_forward
    if ((i+4) <= r) and ''.join(s[i+1:i+4, j]) == "MAS":
        count += 1
    # vertical_backward
    if ((i-3) >= 0) and ''.join(s[i-3:i,j]) == "SAM":
        count += 1
    # Diagonal forward-right
    if i + 4 <= r and j + 4 <= c and ''.join(s[i+k, j+k] for k in range(1, 4)) == "MAS":
        count += 1
    # Diagonal backward-left
    if i - 3 >= 0 and j - 3 >= 0 and ''.join(s[i-k, j-k] for k in range(1, 4)) == "MAS":
        count += 1
    # Diagonal forward-left
    if i + 4 <= r and j - 3 >= 0 and ''.join(s[i+k, j-k] for k in range(1, 4)) == "MAS":
        count += 1
    # Diagonal backward-right
    if i - 3 >= 0 and j + 4 <= c and ''.join(s[i-k, j+k] for k in range(1, 4)) == "MAS":
        count += 1 
    return count    
count = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i, j] == "X":
            count += search_xmas(i, j, s)
print(count)




