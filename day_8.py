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


def generate_anti_nodes(antenna_positions):
    anti_nodes = set()
    for frequency, positions in antenna_positions.items():
        for first in positions:
            for second in positions:
                if first != second:
                    anti_nodes.add(first)
                    anti_nodes.add(second)

                    delta_y = second[1] - first[1]
                    delta_x = second[0] - first[0]

                    x1, y1 = first[0] - delta_x, first[1] - delta_y

                    while in_range(x1, y1):
                        anti_nodes.add((x1, y1))
                        x1, y1 = x1 - delta_x, y1 - delta_y

                    x2, y2 = second[0] + delta_x, second[1] + delta_y

                    while in_range(x2, y2):
                        anti_nodes.add((x2, y2))
                        x2, y2 = x2 + delta_x, y2 + delta_y

    return anti_nodes


print(len(generate_anti_nodes(antenna_positions)))
