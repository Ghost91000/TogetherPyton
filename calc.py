base = input("Введите выражение для вычисления: ")
base = base.replace(' ', '')
outp = base

# base перемннная ввода


# ДОРАБОТАТЬ ВОЗМОЖНОСТЬ ВВОДА ПЕРВОГО ЗНАКА, НАПРИМЕР -1


def str_to_source(inp_string):
    # Функция принимает строку и распределяет ее на массив чисел и массив знаков, возвращает инт число
    begin = 0
    end = 1
    operands = []
    # массив для хранения операндов(чисел)
    operators = []
    # массив для хранения операторов
    while True:
        # print(f"begin = {begin}, end = {end}")
        if end >= len(inp_string):
            operands.append(int(inp_string[begin:end]))
            # выполняется в конце обработки строки, добовляя последнее число
            break
        try:
            """ 
            Этот блок должен ловить ошибки ввода, в случае если введены другие символы кроме чисел и знаков
            Следует доработать функционал поиска ошибок, т.к. Ошибка выводится, но код продолжает выполняться в прежнем режиме
            """
            int(inp_string[begin:end])
        except ValueError:
            print("Вероятно число введено неверно")

        if '+' in inp_string[begin:end + 1]:
            # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
            operators.append(inp_string[end])
            # добовление первого оператора в массив
            operands.append(int(inp_string[begin:end]))
            # доблвление первого операнда
            # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
            # проверка первого оператора
            begin = end + 1
            end = end + 2
            continue

        elif '-' in inp_string[begin:end + 1]:
            # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
            operators.append(inp_string[end])
            # добовление первого оператора в массив
            operands.append(int(inp_string[begin:end]))
            # доблвление первого операнда
            # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
            # проверка первого оператора
            begin = end + 1
            end = end + 2
            continue
        elif '/' in inp_string[begin:end + 1]:
            # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
            operators.append(inp_string[end])
            # добовление первого оператора в массив
            operands.append(int(inp_string[begin:end]))
            # доблвление первого операнда
            # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
            # проверка первого оператора
            begin = end + 1
            end = end + 2
            continue
        elif '*' in inp_string[begin:end + 1]:
            # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
            operators.append(inp_string[end])
            # добовление первого оператора в массив
            operands.append(int(inp_string[begin:end]))
            # доблвление первого операнда
            # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
            # проверка первого оператора
            begin = end + 1
            end = end + 2
            continue

        end = end + 1

    for sign in operators:
        if sign == '*':
            operands[operators.index('*')] *= operands[operators.index('*') + 1]
            del operands[operators.index('*') + 1]
        if sign == '/':
            operands[operators.index('/')] /= operands[operators.index('/') + 1]
            del operands[operators.index('/') + 1]

    i = 1
    # индекс операндов
    ans = operands[0]

    # выполняет операции сложения, вычитания.
    for sign in operators:
        if sign == '+':
            ans += operands[i]
            i += 1
        if sign == '-':
            ans -= operands[i]
            i += 1
    return ans


if '(' in base:
    mass_op = []
    mass_cl = []
    i = 0
    for a in base:
        if a == "(":
            mass_op.append(i)
        elif a == ")":
            mass_cl.append(i)
        i += 1
    assert (len(mass_cl) == len(mass_op)), "Ошибка ввода! Введены неверные скобки"

    op = -1
    cl = 0
    while True:
        ind_begin = base.rfind('(')
        ind_end = base.find(')', ind_begin)

        print(base[ind_begin + 1:ind_end])
        base = base[0:ind_begin] + str(str_to_source(base[ind_begin + 1:ind_end])) + base[ind_end + 1:len(base)]
        print(base)

        cl += 1
        if cl >= len(mass_cl):
            break

base = str_to_source(base)

print(f"{outp} = {base}")

# ans = str_to_source(base)
# print(f"{base} = {ans}")
