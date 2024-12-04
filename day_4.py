letters = []
xmas = ['X', 'M', 'A', 'S']
directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]


def found_in_direction(x, y, letters, direction):
    n = len(letters)
    if x == 0 and y == 5:
        pass
    for i in range(len(xmas)):
        if x < 0 or y < 0 or x >= n or y >= n or letters[x][y] != xmas[i]:
            return False
        x += direction[0]
        y += direction[1]
    return True


def count_in_position(x, y, letters):
    count = 0
    for direction in directions:
        if found_in_direction(x, y, letters, direction):
            count += 1
    return count


with open('day_4.txt') as ifile:
    for line in ifile:
        level = [x for x in line.strip()]
        letters.append(level)

total_count = 0

for i in range(len(letters)):
    for j in range(len(letters[i])):
        total_count += count_in_position(i, j, letters)

print(total_count)
