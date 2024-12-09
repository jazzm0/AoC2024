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
        while disk[start] != -1:
            start += 1
        while disk[end] == -1:
            end -= 1
        if start < end:
            disk[start] = disk[end]
            disk[end] = -1
    return disk


def calc_checksum(disk):
    checksum = 0
    for index in range(len(disk)):
        if disk[index] == -1:
            continue
        checksum += index * disk[index]
    return checksum


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
    for i in range(len(disk)):
        length = 0
        if disk[i] == -1:
            for j in range(i, len(disk)):
                if disk[j] == -1:
                    length += 1
                else:
                    break
        if length >= required_length:
            return i
    return -1


def swap(disk, start_of_free, start_of_section, length):
    copied = 0
    for index in range(start_of_free, start_of_free + length):
        disk[index] = disk[start_of_section + copied]
        disk[start_of_section + copied] = -1
        copied += 1


def compact_2(disk):
    element_id = disk[-1]
    
    while element_id > 0:
        start_of_section, length = find_start_of_move_section(disk, element_id)
        start_of_free = find_free_space(disk, length)
        if 0 < start_of_free < start_of_section:
            swap(disk, start_of_free, start_of_section, length)
        element_id -= 1
    return disk


print(calc_checksum(compact(disk.copy())))
print(calc_checksum(compact_2(disk.copy())))
