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

for i in range(100):
    positions = move(positions, velocities, width, height)
postion_counts = Counter()

for position in positions:
    postion_counts[position] += 1

quadrants = [0, 0, 0, 0]
for position, count in postion_counts.items():
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
