towels = None
designs = []
with open('day_19.txt') as ifile:
    for line in ifile:
        if not towels:
            towels = [x.strip() for x in line.strip().split(",")]
        else:
            line = line.strip()
            if len(line) > 0:
                designs.append(line.strip())


def can_construct(towels, design, memo=None):
    if memo is None:
        memo = {}

    if design == "":
        return 1

    if design in memo:
        return memo[design]

    total_ways = 0
    for towel in towels:
        if design.startswith(towel):
            total_ways += can_construct(towels, design[len(towel):], memo)

    memo[design] = total_ways
    return total_ways


count = 0
total_ways = 0
for design in designs:
    ways = can_construct(towels, design)
    if ways > 0:
        count += 1
        total_ways += ways

print(count)
print(total_ways)
