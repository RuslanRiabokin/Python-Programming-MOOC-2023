# Write your solution here
def filter_solutions():
    correct_file = "correct.csv"
    incorrect_file = "incorrect.csv"
    solutions_file = "solutions.csv"

    try:
        with open(solutions_file, 'r') as input_file, \
             open(correct_file, 'w') as correct_output, \
             open(incorrect_file, 'w') as incorrect_output:

            for line in input_file:
                # Разбиваем строку на части: имя студента, задача и результат
                parts = line.strip().split(';')
                name, problem, result = parts

                # Вычисляем результат операции
                if '+' in problem:
                    operand1, operand2 = map(int, problem.split('+'))
                    actual_result = operand1 + operand2
                elif '-' in problem:
                    operand1, operand2 = map(int, problem.split('-'))
                    actual_result = operand1 - operand2
                else:
                    # Пропускаем строки с некорректной операцией
                    continue

                # Сравниваем результат с ожидаемым и записываем в соответствующий файл
                if actual_result == int(result):
                    correct_output.write(line)
                else:
                    incorrect_output.write(line)

    except FileNotFoundError:
        print("File not found.")

# Вызываем функцию для фильтрации
filter_solutions()

