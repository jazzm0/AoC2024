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


def convert_path(path):
    return ''.join(path) + 'A'


def convert_paths_to_sequence(paths):
    sequences = []
    for path in paths:
        new_sequences = []
        for i in range(len(path)):
            if not sequences:
                new_sequences.append(convert_path(path[i]))
            else:
                for s in sequences:
                    new_sequences.append(s + convert_path(path[i]))
        sequences = new_sequences
    return sequences


def filter_sequences(sequences):
    min_length = min(len(seq) for seq in sequences)
    return [seq for seq in sequences if len(seq) == min_length]


total_value = 0
for code in codes:
    sequences = convert_paths_to_sequence(get_moves(code, keypad))

    for _ in range(2):
        next_sequences = []
        for s in sequences:
            next_sequences.extend(convert_paths_to_sequence(get_moves(s, directions_keypad)))
        sequences = filter_sequences(next_sequences)

    total_value += len(sequences[0]) * int(code[:-1])

print(total_value)
