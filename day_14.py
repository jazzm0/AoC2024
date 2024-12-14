from collections import Counter

positions, velocities = [], []
with open('day_14.txt') as ifile:
    for line in ifile:
        line = line.strip().split(" ")
        position = line[0][2:].split(",")
        velocity = line[1][2:].split(",")
        positions.append((int(position[1]), int(position[0])))
        velocities.append((int(velocity[1]), int(velocity[0])))


def move(positions, velocities, width, height):
    new_positions = []
    for index, position in enumerate(positions):
        new_positions.append(
            ((position[0] + velocities[index][0]) % height, (position[1] + velocities[index][1]) % width))
    return new_positions


# width, height = 11, 7
width, height = 101, 103
original_positions = positions.copy()
for i in range(100):
    positions = move(positions, velocities, width, height)
position_counts = Counter()

for position in positions:
    position_counts[position] += 1

quadrants = [0, 0, 0, 0]
for position, count in position_counts.items():
    half_width, half_height = width // 2, height // 2
    if position[0] == half_height or position[1] == half_width:
        continue
    if position[0] < half_height and position[1] < half_width:
        quadrants[0] += count
    elif position[0] < half_height and position[1] > half_width:
        quadrants[1] += count
    elif position[0] > half_height and position[1] < half_width:
        quadrants[2] += count
    elif position[0] > half_height and position[1] > half_width:
        quadrants[3] += count

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


def print_positions(positions, width, height):
    positions = set(positions)
    for y in range(height):
        line = ""
        for x in range(width):
            if (y, x) in positions:
                line += '*'
            else:
                line += '.'
        print(line)


def count_symmetric(positions, width, height):
    count_symmetry = 0
    positions = set(positions)
    for y in range(height):
        for x in range(width):
            if (y, x) in positions and (y, width - x) in positions:
                count_symmetry += 1
    return count_symmetry


positions = original_positions
# position_tracker = [set() for i in range(len(positions))]
# position_length_tracker = [0 for i in range(len(positions))]
max_symetry_count = 0
for i in range(height * width + 1):
    #    one_changed = False
    #    for index, position in enumerate(positions):
    #        position_tracker[index].add(position)
    #        if position_length_tracker[index] != len(position_tracker[index]):
    #            position_length_tracker[index] = len(position_tracker[index])
    #            if not one_changed:
    #                one_changed = True
    positions = move(positions, velocities, width, height)
    #   if not one_changed:
    max_symetry_count = max(max_symetry_count, count_symmetric(positions, width, height))
    if max_symetry_count == 104:
        print_positions(positions, width, height)
        print(i + 1)
        break
