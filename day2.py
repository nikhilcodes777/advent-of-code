FILE = "inputs/day2.txt"
def get_inputs(filename):
    reports = []
    with open(filename) as file:
        for line in file:
            report = list(map(int,line.split()))
            reports.append(report)
    return reports
def check_safety(report):
    if not (report == sorted(report) or report == sorted(report)[::-1]):
        return False
    for i in range(len(report) - 1):
        delta = abs(report[i] - report[i+1])
        if delta not in (1,2,3):
            return False
    return True

def solve_part1(reports):
    sum = 0
    for report in reports:
        if check_safety(report):
            sum +=1
        

    return sum
reports = get_inputs(FILE)

print(solve_part1(reports))
