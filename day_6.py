guard_map = []
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r, x, y = 0, 0, 0

with open('day_6.txt') as ifile:
    for line in ifile:
        row = [x for x in line.strip()]
        guard_map.append(row)
        column = line.find("^")
        if column > 0:
            y = column
            x = r
        r += 1


def is_valid(position):
    return 0 <= position[0] < len(guard_map) and 0 <= position[1] < len(guard_map[0])


def generate_paths(current_position):
    direction_index = 0
    visited_places = {current_position}
    current_track = {(current_position, direction_index)}

    while True:
        direction = directions[direction_index % 4]
        new_spot = (current_position[0] + direction[0], current_position[1] + direction[1])
        if not is_valid(new_spot):
            return False, visited_places
        else:
            if guard_map[new_spot[0]][new_spot[1]] == "#":
                direction_index = (direction_index + 1) % 4
            else:
                current_position = new_spot
                if (current_position, direction_index) not in current_track:
                    current_track.add((current_position, direction_index))
                else:
                    return True, visited_places
                visited_places.add(current_position)


start = (x, y)

_, visited = generate_paths(start)

print(len(visited))
counter = 0

for x, y in visited:
    guard_map[x][y] = '#'
    if generate_paths(start)[0]:
        counter += 1
    guard_map[x][y] = '.'

print(counter)
