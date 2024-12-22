codes = []
keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1),
          '3': (2, 2), '0': (3, 1), 'A': (3, 2)}

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
directions_keypad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

with open('day_21.txt') as ifile:
    for line in ifile:
        line = line.strip()
        code = []
        for c in line:
            code.append(c)
        codes.append(code)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_keypad_moves(code):
    current = keypad['A']
    moves = []
    for c in code:
        target = keypad[c]
        while current != target:
            for d, delta in directions.items():
                next = (current[0] + delta[0], current[1] + delta[1])
                if distance(next, target) < distance(current, target):
                    moves.append(d)
                    current = next
                    break
        moves.append('A')
        current = target
    return moves


for code in codes:
    print(get_keypad_moves(code))
