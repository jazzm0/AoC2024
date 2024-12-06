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


def generate_paths(current_position, direction_index, visited_places, current_track=None):
    visited_places.add(current_position)
    if not current_track:
        current_track = {(current_position, direction_index)}

    while True:
        direction = directions[direction_index % 4]
        new_spot = (current_position[0] + direction[0], current_position[1] + direction[1])
        if not is_valid(new_spot):
            return False
        else:
            if guard_map[new_spot[0]][new_spot[1]] == "#":
                direction_index = (direction_index + 1) % 4
            else:
                current_position = new_spot
                if (current_position, direction_index) not in current_track:
                    current_track.add((current_position, direction_index))
                else:
                    return True
                visited_places.add(current_position)


start = (x, y)
visited = set()
di = 0

generate_paths(start, di, visited)

print(len(visited))
counter = 0

for v in visited:
    guard_map[v[0]][v[1]] = '#'
    if generate_paths(start, di, set()):
        counter += 1
    guard_map[v[0]][v[1]] = '.'

print(counter)
