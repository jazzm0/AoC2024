from collections import Counter

numbers = []

with open('day_11.txt') as ifile:
    for line in ifile:
        numbers = [int(x) for x in line.strip().split(" ")]


def blink(number_counts):
    new_number_counts = Counter()
    for number, count in number_counts.items():
        length = len(str(number))
        if number == 0:
            new_number_counts[1] += count
        elif length % 2 == 0:
            high, low = int(str(number)[:length // 2]), int(str(number)[length // 2:])
            new_number_counts[high] += count
            new_number_counts[low] += count
        else:
            new_number_counts[number * 2024] += count
    return new_number_counts


number_counts = Counter(numbers)
for i in range(75):
    number_counts = blink(number_counts)

counts = 0
for number, amount in number_counts.items():
    counts += amount

print(counts)
