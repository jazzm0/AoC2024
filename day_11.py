numbers = []

with open('day_11.txt') as ifile:
    for line in ifile:
        numbers = [int(x) for x in line.strip().split(" ")]


def blink(numbers):
    new_numbers = []
    for number in numbers:
        length = len(str(number))
        if number == 0:
            new_numbers.append(1)
        elif length % 2 == 0:
            new_numbers.append(int(str(number)[0:length // 2]))
            new_numbers.append(int(str(number)[length // 2:]))
        else:
            new_numbers.append(number * 2024)
    return new_numbers

for i in range(25):
    numbers = blink(numbers)
    print(numbers)
print(len(numbers))