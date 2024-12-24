from collections import Counter


def calculate(secret):
    n = 64 * secret
    secret ^= n
    secret %= 16777216
    n = secret // 32
    secret ^= n
    secret %= 16777216
    n = secret * 2048
    secret ^= n
    return secret % 16777216


def get_2000(number, sequence_counter):
    price_changes = []
    for i in range(2000):
        old_value = int(str(number)[-1])
        number = calculate(number)
        new_value = int(str(number)[-1])
        price_changes.append(new_value - old_value)
        if i > 2:
            sequence = tuple(price_changes[i - 3:i + 1])
            sequence_counter[sequence] += 1
    return number


total = 0
sequence_counter = Counter()
with open('day_22_small.txt') as ifile:
    for number in ifile:
        total += get_2000(int(number.strip()), sequence_counter)

print(total)
