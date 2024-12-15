import re

directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
map, moves = [], []
start = None
row = 0
with open('day_15.txt') as ifile:
    for line in ifile:
        line = line.strip()
        if line.find("#") >= 0:
            map.append([x for x in line])
            column = line.find("@")
            if column >= 0:
                start = (row, column)
            row += 1
        elif re.search("[^v<>]", line):
            moves.extend([x for x in line if x in directions.keys()])


def is_valid(map, position):
    return 0 <= position[0] < len(map) and 0 <= position[1] < len(map[0])


def can_move(position, map, move):
    direction = directions[move]
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_valid(map, position) or map[new_position[0]][new_position[1]] == "#":
            return False
        elif map[new_position[0]][new_position[1]] == ".":
            return True
        position = new_position


def move_boxes(position, map, move):
    direction = directions[move]
    shift = False
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_valid(map, position) or map[new_position[0]][new_position[1]] == "#":
            break
        elif map[new_position[0]][new_position[1]] == ".":
            map[new_position[0]][new_position[1]] = "O"
            if not shift:
                map[position[0]][position[1]] = "."
            break
        elif map[new_position[0]][new_position[1]] == "O" and not shift:
            shift = True
            map[position[0]][position[1]] = "."
        position = new_position


def execute(position, map, move):
    new_position = (position[0] + directions[move][0], position[1] + directions[move][1])
    if not is_valid(map, position):
        return position
    if map[new_position[0]][new_position[1]] == "#":
        return position
    elif map[new_position[0]][new_position[1]] == ".":
        return new_position
    elif map[new_position[0]][new_position[1]] == "O":
        if can_move(new_position, map, move):
            move_boxes(new_position, map, move)
            return new_position
        else:
            return position
    return position


position = start
for move in moves:
    new_position = execute(position, map, move)
    if new_position != position:
        map[position[0]][position[1]] = "."
        map[new_position[0]][new_position[1]] = "@"
        position = new_position

sum = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == "O":
            sum += r * 100 + c

print(sum)
