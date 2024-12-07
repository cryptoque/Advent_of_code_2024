def main():
    with open("input.txt", "r") as file:
        reports = [list(map(int,line.strip().split())) for line in file]
    safe_count = 0
    safe_with_dampener_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
            safe_with_dampener_count += 1
        elif is_safe_with_dampener(report):
            safe_with_dampener_count += 1
    
    print(safe_count, safe_with_dampener_count)
def if_in_range(a, b):
    return 1 <= a-b <=3

def is_safe(report, order=""):
	if len(report)<=1:
		return True
	if not order:
		order = "d" if report[0]>report[1] else "a"
	if (report[0] > report[1] and order == "d" and if_in_range(report[0], report[1])) or (report[0] < report[1] and order == "a" and if_in_range(report[1], report[0])):
		return is_safe(report[1:], order)
	else:
		return False

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

if __name__ == "__main__":
	main()		
