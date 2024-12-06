map = []
visited = set()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r, x, y = 0, 0, 0

with open('day_6.txt') as ifile:
    for line in ifile:
        row = [x for x in line.strip()]
        map.append(row)
        column = line.find("^")
        if column > 0:
            y = column
            x = r
        r += 1

visited.add((x, y))
current_spot = (x, y)
di = 0
while True:
    direction = directions[di % 4]
    new_spot = (current_spot[0] + direction[0], current_spot[1] + direction[1])
    if not (0 <= new_spot[0] < len(map) and 0 <= new_spot[1] < len(map[0])):
        break
    else:
        if map[new_spot[0]][new_spot[1]] == "#":
            di += 1
        else:
            current_spot = new_spot
            visited.add(current_spot)

print(len(visited))
