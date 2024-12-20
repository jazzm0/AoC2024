prizes = {}
new_prizes = {}
offset = 10 ** 13

increment_a, increment_b = None, None
with open('day_13.txt') as ifile:
    for line in ifile:
        line = line.strip()

        if line.find("Button A:") != -1:
            increments = line.replace("Button A:", "").strip().split(",")
            increment_a = (int(increments[0].strip()[2:]), int(increments[1].strip()[2:]))
        elif line.find("Button B:") != -1:
            increments = line.replace("Button B:", "").strip().split(",")
            increment_b = (int(increments[0].strip()[2:]), int(increments[1].strip()[2:]))
        elif line.find("Prize:") != -1:
            prize_coords = line.replace("Prize:", "").strip().split(",")
            prize = (int(prize_coords[0].strip()[2:]), int(prize_coords[1].strip()[2:]))
            new_prize = (int(prize_coords[0].strip()[2:]) + offset, int(prize_coords[1].strip()[2:]) + offset)
            if increment_a and increment_b:
                prizes[prize] = (increment_a, increment_b)
                new_prizes[new_prize] = (increment_a, increment_b)
                increment_a, increment_b = None, None


def solve(x1, y1, x2, y2, x3, y3):
    alpha = (x3 * y2 - x2 * y3) // (x1 * y2 - x2 * y1)
    beta = (y3 - alpha * y1) // y2
    if alpha and beta and alpha * x1 + beta * x2 == x3 and alpha * y1 + beta * y2 == y3:
        return alpha, beta
    return None, None


total_cost = 0

for prize, buttons in prizes.items():
    a, b = solve(buttons[0][0], buttons[0][1], buttons[1][0], buttons[1][1], prize[0], prize[1])
    if a and b:
        total_cost += 3 * a + b

print(total_cost)

total_cost = 0

for prize, buttons in new_prizes.items():
    a, b = solve(buttons[0][0], buttons[0][1], buttons[1][0], buttons[1][1], prize[0], prize[1])
    if a and b:
        total_cost += 3 * a + b

print(total_cost)
