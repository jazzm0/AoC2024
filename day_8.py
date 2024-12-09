antenna_positions = {}

row = 0
column = 0

with open('day_8.txt') as ifile:
    for line in ifile:
        line = line.strip()
        column = len(line)
        for c in range(column):
            if line[c] != '.':
                positions = antenna_positions.get(line[c], set())
                positions.add((row, c))
                antenna_positions[line[c]] = positions
        row += 1


def in_range(x, y):
    return 0 <= x < column and 0 <= y < row


def generate_antinodes(antenna_positions):
    antinodes = set()
    for frequency, positions in antenna_positions.items():
        for first in positions:
            for second in positions:
                if first != second:
                    
                    delta_y = second[1] - first[1]
                    delta_x = second[0] - first[0]

                    x1, y1 = first[0] - delta_x, first[1] - delta_y

                    if in_range(x1, y1) and (x1, y1) not in positions:
                        antinodes.add((x1, y1))

                    x2, y2 = second[0] + delta_x, second[1] + delta_y

                    if in_range(x2, y2) and (x2, y2) not in positions:
                        antinodes.add((x2, y2))

    return antinodes


print(len(generate_antinodes(antenna_positions)))
