rules = {}
updates = []

with open('day_5.txt') as ifile:
    for line in ifile:
        line = line.strip()
        if line.find("|") > 0:
            x, y = line.split("|")
            pages = rules.get(int(x), set())
            pages.add(int(y))
            rules[int(x)] = pages
        elif line.find(",") > 0:
            update = line.split(",")
            updates.append([int(x) for x in update])


def check_correct_order(update, rules):
    for i in range(len(update) - 1):
        if update[i + 1] not in rules.get(update[i], set()):
            return False
    return True


result = 0

for update in updates:
    if check_correct_order(update, rules):
        result += update[len(update) // 2]

print(result)
