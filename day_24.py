from pyvis.network import Network


def parse_input():
    wire_values = {}
    operations = []

    with open('day_24.txt') as ifile:
        for line in ifile:
            if ':' in line:
                wire, value = line.split(':')
                wire_values[wire.strip()] = int(value.strip())
            elif '->' in line:
                parts = line.split('->')
                operation = parts[0].strip()
                output_wire = parts[1].strip()
                operations.append((operation, output_wire))

    return wire_values, operations


def evaluate_operation(operation, wire_values):
    op1, gate, op2 = operation.split()
    op1_value = wire_values[op1]
    op2_value = wire_values[op2]

    # Perform the gate operation
    if gate == "AND":
        return op1_value & op2_value
    elif gate == "OR":
        return op1_value | op2_value
    elif gate == "XOR":
        return op1_value ^ op2_value


def simulate_gates(wire_values, operations):
    while operations:
        remaining_operations = []
        for operation, output_wire in operations:
            operands = operation.split()
            op1, op2 = operands[0], operands[2]

            if op1 in wire_values and op2 in wire_values:
                wire_values[output_wire] = evaluate_operation(operation, wire_values)
            else:
                remaining_operations.append((operation, output_wire))

        if len(remaining_operations) == len(operations):
            break

        operations = remaining_operations
    return wire_values


def plot(output: str, operations: list):
    net = Network()
    added_nodes = set()

    for operation in operations:
        target = operation[1]
        in1, gate, in2 = operation[0].split()

        if in1 not in added_nodes:
            net.add_node(in1, label=in1)
            added_nodes.add(in1)

        if in2 not in added_nodes:
            net.add_node(in2, label=in2)
            added_nodes.add(in2)

        if target not in added_nodes:
            net.add_node(target, label=f"{gate} {target}", shape="box")
            added_nodes.add(target)

        net.add_edge(in1, target)
        net.add_edge(in2, target)

    net.toggle_physics(True)
    net.show(output, notebook=False)


wire_values, operations = parse_input()

plot("24.html", operations)

wire_values = simulate_gates(wire_values, operations)

output_value = 0
bit_position = 0
while f"z{bit_position:02d}" in wire_values:
    output_value += wire_values[f"z{bit_position:02d}"] << bit_position
    bit_position += 1

print(f"Output value: {output_value}")


# problems z30, z17