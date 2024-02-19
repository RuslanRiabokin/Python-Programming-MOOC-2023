def run(program):
    def evaluate_condition(condition, variables):
        operand1, op, operand2 = condition.split()
        operand1 = operand1.strip()
        operand2 = operand2.strip()
        op = op.strip()

        # Fetch values of operands
        val1 = variables[operand1] if operand1.isalpha() else int(operand1)
        val2 = variables[operand2] if operand2.isalpha() else int(operand2)

        # Evaluate condition
        if op == "==":
            return val1 == val2
        elif op == "!=":
            return val1 != val2
        elif op == "<":
            return val1 < val2
        elif op == "<=":
            return val1 <= val2
        elif op == ">":
            return val1 > val2
        elif op == ">=":
            return val1 >= val2
        else:
            raise ValueError("Invalid comparison operator")

    def preprocess_program(program):
        label_map = {}
        for i, line in enumerate(program):
            if line.endswith(":"):
                label = line[:-1]
                label_map[label] = i
        return label_map

    label_map = preprocess_program(program)

    variables = {chr(i): 0 for i in range(65, 91)}  # Initialize variables A-Z
    result = []

    i = 0
    while i < len(program):
        line = program[i].split()

        if line[0] == "PRINT":
            value = variables[line[1]] if line[1].isalpha() else int(line[1])
            result.append(value)
        elif line[0] == "MOV":
            variables[line[1]] = variables[line[2]] if line[2].isalpha() else int(line[2])
        elif line[0] == "ADD":
            variables[line[1]] += variables[line[2]] if line[2].isalpha() else int(line[2])
        elif line[0] == "SUB":
            variables[line[1]] -= variables[line[2]] if line[2].isalpha() else int(line[2])
        elif line[0] == "MUL":
            variables[line[1]] *= variables[line[2]] if line[2].isalpha() else int(line[2])
        elif line[0] in label_map:
            pass  # Labels don't need any execution
        elif line[0] == "JUMP":
            label = line[1]
            if label in label_map:
                i = label_map[label]
            else:
                raise ValueError(f"Label '{label}' not found")
        elif line[0] == "IF":
            condition = " ".join(line[1:-2])
            location = line[-1]
            if evaluate_condition(condition, variables):
                if location in label_map:
                    i = label_map[location]
                else:
                    raise ValueError(f"Label '{location}' not found")
        elif line[0] == "END":
            break

        i += 1

    return result


