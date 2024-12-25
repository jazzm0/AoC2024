connections = {}

with open('day_23.txt') as ifile:
    for connection in ifile:
        computers = connection.strip().split("-")
        connected = connections.setdefault(computers[0], set())
        connected.add(computers[1])
        connected = connections.setdefault(computers[1], set())
        connected.add(computers[0])

threesome = set()
for node, connected in connections.items():
    for neighbour in connected:
        for second_neighbour in connections[neighbour]:
            if second_neighbour != node and node in connections[second_neighbour]:
                three = sorted([node, neighbour, second_neighbour])
                threesome.add(tuple(three))

counter = 0
for a, b, c in threesome:
    if a.find("t") == 0 or b.find("t") == 0 or c.find("t") == 0:
        counter += 1
print(counter)
