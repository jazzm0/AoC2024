disk_map = ""

with open('day_9.txt') as ifile:
    for line in ifile:
        disk_map = line.strip()

disk = []
disk_id = 0
for index in range(len(disk_map)):
    if index % 2 == 0:
        disk.extend([x for x in [disk_id] * int(disk_map[index])])
        disk_id += 1
    else:
        disk.extend([x for x in [-1] * int(disk_map[index])])


def compact(disk):
    start, end = 0, len(disk) - 1
    while start < end:
        while start < end and disk[start] != -1:
            start += 1
        while start < end and disk[end] == -1:
            end -= 1
        if start < end:
            disk[start], disk[end] = disk[end], -1
    return disk


def calc_checksum(disk):
    return sum(index * value for index, value in enumerate(disk) if value != -1)


def find_start_of_move_section(disk, element_id):
    start, length = 0, 0
    for start in range(len(disk)):
        if disk[start] == element_id:
            break
    end = start
    while end < len(disk) and disk[end] == element_id:
        length += 1
        end += 1
    return start, length


def find_free_space(disk, required_length):
    length = 0
    for i, value in enumerate(disk):
        if value == -1:
            length += 1
            if length >= required_length:
                return i - required_length + 1
        else:
            length = 0
    return -1


def compact_2(disk):
    element_id = max(disk)
    while element_id > 0:
        start_of_section = disk.index(element_id)
        length = disk[start_of_section:].count(element_id)
        start_of_free = find_free_space(disk, length)
        if 0 < start_of_free < start_of_section:
            for i in range(length):
                disk[start_of_free + i], disk[start_of_section + i] = disk[start_of_section + i], -1
        element_id -= 1
    return disk


print(calc_checksum(compact(disk.copy())))
print(calc_checksum(compact_2(disk.copy())))
