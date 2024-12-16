map = []

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
direction_names = ['U', 'D', 'R', 'L']
start, end = None, None
row = 0

with open('day_16_small.txt') as ifile:
    for line in ifile:
        map.append([x for x in line.strip()])
        column = line.find("S")
        if column >= 0:
            start = (row, column)
        column = line.find("E")
        if column >= 0:
            end = (row, column)
        row += 1


def get_next_positions(map, position, visited):
    next_positions = []
    if position == end:
        return next_positions
    for i, direction in enumerate(directions):
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if 0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0]) and map[new_position[0]][new_position[1]] != "#" and new_position not in visited:
            next_positions.append((new_position, direction_names[i]))
    return next_positions


def finished(routes):
    for route in routes:
        if route[0] != end:
            return False
    return True


routes = [(start, {start}, 0, 'R', 0)]  # (current_position, visited_positions, steps, last_direction, turns)

while not finished(routes):
    new_routes = []
    for route in routes:
        next_positions = get_next_positions(map, route[0], route[1])
        for next_position, direction in next_positions:
            new_visited = set(route[1])
            new_visited.add(next_position)
            turns = route[4] + (1 if route[3] and route[3] != direction else 0)
            new_routes.append((next_position, new_visited, route[2] + 1, direction, turns))
        if route[0] == end:
            new_routes.append(route)
    routes = new_routes

# Filter the routes to find the one with the minimum turns
min_turns_route = min(routes, key=lambda x: (x[4], x[2]))
print(f"Route: {min_turns_route[0]}, Steps: {min_turns_route[2]}, Turns: {min_turns_route[4]}")
print(min_turns_route[2] + 1000 * min_turns_route[4])