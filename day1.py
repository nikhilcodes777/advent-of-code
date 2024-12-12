FILE="inputs/day1.txt"
def split_digits_from_file(filename):
    left_digits = []
    right_digits = []

    with open(filename) as file:
        for line in file:
            left, right = map(int, line.split())
            left_digits.append(left)
            right_digits.append(right)

    return sorted(left_digits), sorted(right_digits)


def solve_recursion(left, right, sum=0):
    if not left or not right:  
        return sum
    sum += abs(left[0] - right[0])
    return solve(left[1:], right[1:], sum)   

def solve(left, right):
    total_sum = 0
    for l, r in zip(left, right):
        total_sum += abs(l - r)
    return total_sum

left,right = split_digits_from_file(FILE)
print(solve(left,right))
