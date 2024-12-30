keys, locks = [], []

i = 0
object = []


def convert(keys, locks, object):
    pin_count = [-1] * 5
    is_lock = all(x == "#" for x in object[0])
    for i in range(len(object)):
        for j in range(len(object[i])):
            if object[i][j] == "#":
                pin_count[j] += 1
    if is_lock:
        locks.append(tuple(pin_count))
    else:
        keys.append(tuple(pin_count))


with open('day_25.txt') as ifile:
    for pins in ifile:
        if i % 7 == 0 and i != 0:
            convert(keys, locks, object)
            object = []
            i = 0
        else:
            object.append([x for x in pins.strip()])
            i += 1

convert(keys, locks, object)

fits = set()

for key in keys:
    for lock in locks:
        fit = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                fit = False
                break
        if fit:
            fits.add((lock, key))

print(len(fits))
