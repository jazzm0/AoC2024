directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
topographical_map = []
starts = set()

row = 0
with open('day_10.txt') as ifile:
    for line in ifile:
        topographical_map.append([int(x) for x in line.strip()])
        for column, value in enumerate(topographical_map[-1]):
            if value == 0:
                starts.add((row, column))
        row += 1


def get_trailheads(start, distinct_paths):
    next_location_value = 0
    current_locations = {start}
    paths = [[start]]
    while current_locations:
        next_locations = set()
        next_location_value += 1
        reachable_from_location = {}
        for direction in directions:
            for location in current_locations:
                row, column = location
                new_row, new_column = row + direction[0], column + direction[1]
                if 0 <= new_row < len(topographical_map) and 0 <= new_column < len(topographical_map[0]) and \
                        topographical_map[new_row][new_column] == next_location_value:
                    next_locations.add((new_row, new_column))
                    reachable_from_location.setdefault(location, set()).add((new_row, new_column))

        paths = [path + [loc] for path in paths for loc in next_locations if
                 path[-1] in reachable_from_location and loc in reachable_from_location[path[-1]]]

        current_locations = next_locations

        if next_location_value == 9:
            for path in paths:
                distinct_paths.add(tuple(path))
            return len(next_locations)


total_trailheads = 0
distinct_paths = set()
for start in starts:
    total_trailheads += get_trailheads(start, distinct_paths)

print(total_trailheads)
print(len(distinct_paths))
