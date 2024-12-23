from collections import deque

codes = []
keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1),
          '3': (2, 2), '0': (3, 1), 'A': (3, 2)}

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
directions_keypad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

with open('day_21.txt') as ifile:
    for line in ifile:
        code = line.strip()
        codes.append(code)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_moves(sequence, pad):
    start = pad['A']
    valid_positions = set(pad.values())
    all_paths = []

    def bfs(start, target):
        queue = deque([(start, [])])
        visited = {}
        shortest_paths = []

        while queue:
            current, path = queue.popleft()

            if current == target:
                if not shortest_paths or len(path) == len(shortest_paths[0]):
                    shortest_paths.append(path)
                elif len(path) < len(shortest_paths[0]):
                    shortest_paths = [path]
                continue

            if current in visited and len(path) > visited[current]:
                continue
            visited[current] = len(path)

            for d, delta in directions.items():
                next_pos = (current[0] + delta[0], current[1] + delta[1])
                if next_pos in valid_positions:
                    queue.append((next_pos, path + [d]))

        return shortest_paths

    current = start
    for s in sequence:
        target = pad[s]
        paths = bfs(current, target)
        all_paths.append(paths)
        current = target

    return all_paths


total_value = 0
total_moves = []
for code in codes:
    keypad_moves = get_moves("029A", keypad)
    second_sequence = get_moves(keypad_moves, directions_keypad)
    third_sequence = get_moves(second_sequence, directions_keypad)
    code_value = int(code[0:-1])
