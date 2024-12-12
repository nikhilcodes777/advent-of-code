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


def check_safety_part2(report):
    if check_safety(report):
        return True
    else:
        for i in range(len(report)):
            poppedlist = report[:i] + report[i+1:]
            if check_safety(poppedlist):
                return True
    return False

def solve(reports,safety_function):
    sum = len(list(filter(safety_function,reports)))
    return sum
reports = get_inputs(FILE)

print("Solution to part 1 :> ",solve(reports,check_safety))
print("Solution to part 2 :> ",solve(reports,check_safety_part2))
