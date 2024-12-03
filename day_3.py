import re


def mul(s):
    nums = s[4:-1].split(',')
    return int(nums[0]) * int(nums[1])


def calculate_value(line):
    total_value = 0
    for num in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line):
        total_value += mul(num)
    return total_value


total = 0
with open('day_3.txt') as ifile:
    for line in ifile:
        total += calculate_value(line)

print(total)
