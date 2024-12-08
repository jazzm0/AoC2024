from math import sqrt

antenna_positions = {}

row = 0
with open('day_8_small.txt') as ifile:
    for line in ifile:
        line = line.strip()
        for c in range(len(line)):
            if line[c] != '.':
                positions = antenna_positions.get(line[c], set())
                positions.add((row, c))
                antenna_positions[line[c]] = positions
        row += 1


def generate_antinodes(antenna_positions):
    antinodes = set()
    for frequency, positions in antenna_positions.items():
        for first in positions:
            for second in positions:
                if first != second:
                    delta_y = second[1] - first[1]
                    delta_x = second[0] - first[0]
                    distance = sqrt(delta_x ** 2 + delta_y ** 2)
                    b = first[1] / (first[0] * delta_y) / delta_x
                    print(distance)
    return antinodes


print(generate_antinodes(antenna_positions))
