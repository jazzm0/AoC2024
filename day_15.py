import re

directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
opposite = {"<": ">", ">": "<", "^": "v", "v": "^"}
brackets = {"[", "]"}
warehouse, big_warehouse, moves = [], [], []
start, new_start = None, None
row = 0
with open('day_15_big_move.txt') as ifile:
    for line in ifile:
        line = line.strip()
        if line.find("#") >= 0:
            warehouse.append([x for x in line])
            big_line = []
            for x in line:
                if x == ".":
                    big_line.extend([".", "."])
                elif x == "#":
                    big_line.extend(["#", "#"])
                elif x == "O":
                    big_line.extend(["[", "]"])
                elif x == "@":
                    big_line.extend(["@", "."])
                    for i in range(len(big_line)):
                        if big_line[i] == "@":
                            break
            big_warehouse.append(big_line)
            column = line.find("@")
            if column >= 0:
                start = (row, column)
                new_start = (row, column * 2)
            row += 1
        elif re.search("[^v<>]", line):
            moves.extend([x for x in line if x in directions.keys()])


def is_valid(warehouse, position):
    return 0 <= position[0] < len(warehouse) and 0 <= position[1] < len(warehouse[0])


def check_line(warehouse, left, right):
    only_boxes = True
    while left != right:
        if warehouse[left[0]][left[1]] not in brackets:
            only_boxes = False
            if warehouse[left[0]][left[1]] == "#" or warehouse[right[0]][right[1]] == "#":
                return -1
        left = (left[0] + directions[">"][0], left[1] + directions[">"][1])
    if only_boxes:
        return 1
    return 0


def get_line_endings(warehouse, position):
    left, right = position, position

    while True:
        new_left, new_right = (left[0] + directions["<"][0], left[1] + directions["<"][1]), (
            right[0] + directions[">"][0], right[1] + directions[">"][1])
        if is_valid(warehouse, new_left) and warehouse[new_left[0]][new_left[1]] in brackets:
            left = new_left
        if is_valid(warehouse, new_right) and warehouse[new_right[0]][new_right[1]] in brackets:
            right = new_right
        if left != new_left and right != new_right:
            return left, right


def can_move(position, warehouse, move, is_small=True):
    direction = directions[move]
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_valid(warehouse, position) or warehouse[new_position[0]][new_position[1]] == "#":
            return False
        elif warehouse[new_position[0]][new_position[1]] == "." and (is_small or move == "<" or move == ">"):
            return True
        elif not is_small and (move == "^" or move == "v"):
            left, right = get_line_endings(warehouse, position)
            left, right = (left[0] + directions[move][0], left[1] + directions[move][1]), (
                right[0] + directions[move][0], right[1] + directions[move][1])
            available = check_line(warehouse, left, right)
            if available == -1:
                return False
            elif available == 0:
                return True
        position = new_position


def move_boxes(position, warehouse, move):
    direction = directions[move]
    shift = False
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_valid(warehouse, position) or warehouse[new_position[0]][new_position[1]] == "#":
            break
        elif warehouse[new_position[0]][new_position[1]] == ".":
            warehouse[new_position[0]][new_position[1]] = "O"
            if not shift:
                warehouse[position[0]][position[1]] = "."
            break
        elif warehouse[new_position[0]][new_position[1]] == "O" and not shift:
            shift = True
            warehouse[position[0]][position[1]] = "."
        position = new_position


def move_big_boxes_horizontal(warehouse, position, move):
    direction = directions[move]
    source = position
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_valid(warehouse, position) or warehouse[new_position[0]][new_position[1]] == "#":
            break
        position = new_position
        if warehouse[position[0]][position[1]] == ".":
            break
    while source != position:
        previous = (position[0] + directions[opposite[move]][0], position[1] + directions[opposite[move]][1])
        warehouse[position[0]][position[1]] = warehouse[previous[0]][previous[1]]
        position = previous
    warehouse[position[0]][position[1]] = '.'


def move_big_boxes_vertical(warehouse, position, move):
    direction = directions[move]
    source = None
    left, right = None, None
    while True:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if not source:
            source = new_position
        if not is_valid(warehouse, position) or warehouse[new_position[0]][new_position[1]] == "#":
            break
        if left and right:
            left, right = (left[0] + directions[move][0], left[1] + directions[move][1]), (
                right[0] + directions[move][0], right[1] + directions[move][1])
            available = check_line(warehouse, left, right)
            if available == 0:
                break
        left, right = get_line_endings(warehouse, position)
        position = new_position

    while source != position:
        previous = (position[0] + directions[opposite[move]][0], position[1] + directions[opposite[move]][1])
        left, right = get_line_endings(warehouse, previous)
        while left[1] <= right[1]:
            warehouse[position[0]][left[1]] = warehouse[previous[0]][left[1]]
            warehouse[previous[0]][left[1]] = "."
            left = (left[0] + directions[">"][0], left[1] + directions[">"][1])

        position = previous


def execute(position, warehouse, move):
    new_position = (position[0] + directions[move][0], position[1] + directions[move][1])
    if not is_valid(warehouse, position):
        return position
    element = warehouse[new_position[0]][new_position[1]]
    if element == "#":
        return position
    elif element == ".":
        return new_position
    elif element == "O":
        if can_move(new_position, warehouse, move):
            move_boxes(new_position, warehouse, move)
            return new_position
        else:
            return position
    elif element == "[" or element == "]":
        if can_move(new_position, warehouse, move, False):
            if move == "<" or move == ">":
                move_big_boxes_horizontal(warehouse, new_position, move)
            else:
                move_big_boxes_vertical(warehouse, position, move)
            return new_position
        else:
            return position
    return position


def calculate_gps(warehouse):
    sum = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == "O" or warehouse[r][c] == "[":
                sum += r * 100 + c
    return sum


# position = start
# for move in moves:
#     new_position = execute(position, warehouse, move)
#     if new_position != position:
#         warehouse[position[0]][position[1]] = "."
#         warehouse[new_position[0]][new_position[1]] = "@"
#         position = new_position
#
# print(calculate_gps(warehouse))

position = new_start
for move in moves:
    new_position = execute(position, big_warehouse, move)
    if new_position != position:
        big_warehouse[position[0]][position[1]] = "."
        big_warehouse[new_position[0]][new_position[1]] = "@"
        position = new_position

print(calculate_gps(big_warehouse))
