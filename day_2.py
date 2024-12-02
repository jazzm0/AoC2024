reports = []

with open('day_2.txt') as ifile:
    for line in ifile:
        level = [int(x) for x in line.strip().split(" ")]
        reports.append(level)

safe_count = 0


def is_almost_strictly_monotone(sequence):
    def is_strictly_monotone(seq):
        return all(1 <= abs(x - y) <= 3 and x < y for x, y in zip(seq, seq[1:])) or \
            all(1 <= abs(x - y) <= 3 and x > y for x, y in zip(seq, seq[1:]))

    if is_strictly_monotone(sequence):
        return True

    for i in range(len(sequence)):
        new_sequence = sequence[:i] + sequence[i + 1:]
        if is_strictly_monotone(new_sequence):
            return True

    return False


for level in reports:
    if is_almost_strictly_monotone(level):
        safe_count += 1

print(safe_count)
