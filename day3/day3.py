import re
with open("input.txt", "r") as file:
    content = file.read()
pattern1 = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern2 = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"

matches1 = re.findall(pattern1, content)
matches2 = re.finditer(pattern2, content)

result1 = sum(map(lambda t: int(t[0])*int(t[1]), matches1))

l = []
for match in matches2:
    if match.group(1) and match.group(2):
        l.append(int(match.group(1))*int(match.group(2)))
    elif match.group(3):
        l.append(True)
    elif match.group(4):
        l.append(False)

def is_bool(a):
    return isinstance(a, bool)

result2=0
flag=True
for i in range(len(l)):
    if flag==True and not is_bool(l[i]):
        result2+=l[i]
    elif is_bool(l[i]):
        flag = l[i]

print(result1, result2)
