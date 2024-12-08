equations = []

with open('day_7.txt') as ifile:
    for line in ifile:
        equation = line.strip().split(":")
        equations.append((int(equation[0]), [int(x) for x in equation[1].strip().split(" ")]))


def solve(test_result, numbers):
    results = set()
    results.add(numbers[0])
    previous = numbers[0]
    for i in range(1, len(numbers)):
        new_results = set()
        new_results.add(int(str(previous) + str(numbers[i])))
        previous = numbers[i]
        for r in results:
            new_results.add(r * numbers[i])
            new_results.add(r + numbers[i])
            new_results.add(int(str(r) + str(numbers[i])))
        results = new_results
    return test_result in results


result = 0
for equation in equations:
    if solve(equation[0], equation[1]):
        result += equation[0]

print(result)
