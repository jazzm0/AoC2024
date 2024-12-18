registers = {}
program = []

with open('day_17.txt') as ifile:
    for line in ifile:
        line = line.strip()
        if line.find("Register") != -1:
            parts = line.split(" ")
            registers[parts[1][0]] = int(parts[2])
        elif line.find("Program") != -1:
            for input in line.split(" ")[1].split(","):
                program.append(int(input))


def get_operand(operand, registers):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    elif operand == 7:
        raise Exception("Invalid operand")


def execute(program, registers, output, compare=False):
    ip = 0
    while ip < len(program):
        instruction = program[ip]
        operand = program[ip + 1]

        if instruction == 0:  # adv
            operand = get_operand(operand, registers)
            registers["A"] = registers["A"] // (2 ** operand)
        elif instruction == 1:  # bxl
            registers["B"] ^= operand
        elif instruction == 2:  # bst
            operand = get_operand(operand, registers)
            registers["B"] = operand % 8
        elif instruction == 3:  # jnz
            if registers["A"] != 0:
                ip = operand
                continue
        elif instruction == 4:  # bxc
            registers["B"] ^= registers["C"]
        elif instruction == 5:  # out
            output.append(get_operand(operand, registers) % 8)
            if compare and program[0:len(output)] != output:
                return False
        elif instruction == 6:  # bdv
            operand = get_operand(operand, registers)
            registers["B"] = registers["A"] // (2 ** operand)
        elif instruction == 7:  # cdv
            operand = get_operand(operand, registers)
            registers["C"] = registers["A"] // (2 ** operand)
        ip += 2
    return program == output


def get_matches(program, output):
    match_count = 0
    while match_count < len(output) and program[match_count] == output[match_count]:
        match_count += 1
    return match_count


matches = {}
output = []
execute(program, registers, output)
print(*output, sep=",")

for input in range(1, 10 ** 6):
    registers["A"] = input
    registers["B"] = registers["C"] = 0
    output = []
    result = execute(program, registers, output, True)
    match_count = get_matches(program, output)
    if match_count not in matches:
        matches[match_count] = [input]
    else:
        if len(matches[match_count]) == 10:
            continue
        matches[match_count].append(input)
    if result:
        print(input)
        break

print(matches)
