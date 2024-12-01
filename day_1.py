left, right = [], []
occurrences = {}

with open('day_1.txt') as ifile:
    for line in ifile:
        elements = line.strip().split("   ")
        left.append(int(elements[0]))
        r = int(elements[1])
        right.append(r)
        occurrences[r] = occurrences.get(r, 0) + 1

left, right = sorted(left), sorted(right)

result, score = 0, 0
for i in range(len(left)):
    result += abs(left[i] - right[i])
    score += left[i] * occurrences.get(left[i], 0)

print(result)
print(score)
