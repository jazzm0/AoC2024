disk_map = ""

with open('day_9.txt') as ifile:
    for line in ifile:
        disk_map = line.strip()

disk = []
disk_id = 0
for index in range(len(disk_map)):
    if index % 2 == 0:
        for x in [disk_id] * int(disk_map[index]):
            disk.append(x)
        disk_id += 1
    else:
        for x in [-1] * int(disk_map[index]):
            disk.append(x)

start, end = 0, len(disk) - 1
while start < end:
    while disk[start] != -1:
        start += 1
    while disk[end] == -1:
        end -= 1
    if start < end:
        disk[start] = disk[end]
        disk[end] = -1

checksum = 0
for index in range(len(disk)):
    if disk[index] == -1:
        break
    checksum += index * disk[index]

print(checksum)
