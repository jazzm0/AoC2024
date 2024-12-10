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


def get_trailheads(start):
    next_location_value = 0
    current_locations = {start}
    while True:
        next_locations = set()
        next_location_value += 1
        for direction in directions:
            for location in current_locations:
                row, column = location
                new_row, new_column = row + direction[0], column + direction[1]
                if 0 <= new_row < len(topographical_map) and 0 <= new_column < len(topographical_map[0]) and \
                        topographical_map[new_row][new_column] == next_location_value:
                    next_locations.add((new_row, new_column))

        current_locations = next_locations
        if len(next_locations) == 0:
            return 0
        elif next_location_value == 9:
            return len(next_locations)


total_trailheads = 0
for start in starts:
    total_trailheads += get_trailheads(start)

print(total_trailheads)
