registers = {"A": 0, "B": 0, "C": 0}
program = []

with open('day_17.txt') as ifile:
    for line in ifile:
        line = line.strip()
        if line.find("Register") != -1:
            parts = line.split(" ")
            registers[parts[1][0]] = int(parts[2])
        elif line.find("Program") != -1:
            for i in line.split(" ")[1].split(","):
                program.append(int(i))


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


def execute(program, registers, output):
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
            output.append(str(get_operand(operand, registers) % 8))
        elif instruction == 6:  # bdv
            operand = get_operand(operand, registers)
            registers["B"] = registers["A"] // (2 ** operand)
        elif instruction == 7:  # cdv
            operand = get_operand(operand, registers)
            registers["C"] = registers["A"] // (2 ** operand)
        ip += 2

output = []
execute(program, registers, output)
print(",".join(output))