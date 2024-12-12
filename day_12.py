garden = []
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open('day_12.txt') as ifile:
    for line in ifile:
        garden.append([x for x in line.strip()])


def explore_region(x, y, regions, explored):
    if (x, y) in explored:
        return
    plant_type = garden[x][y]
    region = set()
    next = {(x, y)}
    while next:
        x, y = next.pop()

        region.add((x, y))
        explored.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(garden) and 0 <= new_y < len(garden[0]) and garden[new_x][new_y] == plant_type and (
                    new_x, new_y) not in explored:
                region.add((x, y))
                next.add((new_x, new_y))
                explored.add((new_x, new_y))
    if region:
        regions.append(region)


def calculate_perimeter(region):
    perimeter = 0
    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in region:
                perimeter += 1

    return perimeter


regions = []
explored = set()

for x in range(len(garden)):
    for y in range(len(garden[0])):
        explore_region(x, y, regions, explored)

total_price = 0
for region in regions:
    total_price += len(region) * calculate_perimeter(region)

print(total_price)
