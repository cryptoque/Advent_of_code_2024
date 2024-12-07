# open the file in read mode
with open("input.txt", "r") as file:
	left, right = map(list, zip(*(line.strip().split() for line in file)))
output=0
left = list(map(int, left))
right = list(map(int, right))
left.sort()
right.sort()

output1 = sum(abs(int(a)-int(b)) for a, b in zip(left, right)) 
print(output1)

freq = {}
for element in right:
	freq[element]=freq.get(element, 0) + 1

output2 = sum(element * freq.get(element, 0) for element in left)
print(output2)
