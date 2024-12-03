import re


def mul(s):
    nums = s[4:-1].split(',')
    return int(nums[0]) * int(nums[1])


def find_next_stop(current_position, positions):
    while len(positions) > 1 and positions[0] <= current_position:
        positions.pop(0)

    if positions:
        return positions[0]
    return -1


def calculate_value(program):
    total_value = 0
    starts = [s.start() for s in re.finditer(r"do\(\)", program)]
    ends = [s.start() for s in re.finditer(r"don\'t\(\)", program)]
    enabled = True
    current_position, next_stop = 0, 0
    while True:
        if enabled:
            if ends[-1] == next_stop:
                enabled = True
                next_stop = len(program)
            else:
                next_stop = find_next_stop(current_position, ends)
                enabled = False
        else:
            current_position = find_next_stop(current_position, starts)
            enabled = True
            continue

        for num in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", program[current_position:next_stop]):
            total_value += mul(num)

        current_position = next_stop
        if current_position == len(program):
            break

    return total_value


with open('day_3_2.txt') as ifile:
    program = ifile.read()

print(calculate_value(program))
