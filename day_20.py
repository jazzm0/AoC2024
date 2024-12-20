import heapq

track = []
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
stuck = []

start, end = None, None
row = 0
with open('day_20_small.txt') as ifile:
    for line in ifile:
        line = line.strip()
        track.append([x for x in line])
        start_column = line.find("S")
        if start_column >= 0:
            start = (row, start_column)
        end_column = line.find("E")
        if end_column >= 0:
            end = (row, end_column)

        row += 1


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_next_positions(track, position):
    next_positions = []
    for direction in directions:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if 0 <= new_position[0] < len(track) and 0 <= new_position[1] < len(track[0]) and track[new_position[0]][
            new_position[1]] != "#":
            next_positions.append(new_position)
    return next_positions


def a_star_search(start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_next_positions(track, current):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


path = a_star_search(start, end)
print(len(path) - 1)
