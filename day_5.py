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


def fix_order(update, rules):
    i = 0
    while i < len(update) - 1:
        if update[i + 1] in rules.get(update[i], set()):
            i += 1
        else:
            update[i], update[i + 1], i = update[i + 1], update[i], 0

    return update


first_result, second_result = 0, 0

for update in updates:
    if check_correct_order(update, rules):
        first_result += update[len(update) // 2]
    else:
        update = fix_order(update, rules)
        second_result += update[len(update) // 2]

print(first_result)
print(second_result)
