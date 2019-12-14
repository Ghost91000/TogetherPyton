base = "3+5+6+(5+6)"#i nput("Введите выражение для вычисления: ")
base = base.replace(' ', '')
# base перемннная ввода
operands = []
# массив для хранения операндов(чисел)
operators = []
# массив для хранения операторов
begin = 0
end = 1



# блок обработки строки в массивы, принимает строку и возвращает масссив чисел и знаков
# ДОРАБОТАТЬ ВОЗМОЖНОСТЬ ВВОДА ПЕРВОГО ЗНАКА, НАПРИМЕР -1
while True:
    print(f"begin = {begin}, end = {end}")
    if end >= len(base):
        operands.append(int(base[begin:end]))
        # выполняется в конце обработки строки, добовляя последнее число
        break
    try:
        """ 
        Этот блок должен ловить ошибки ввода, в случае если введены другие символы кроме чисел и знаков
        Следует доработать функционал поиска ошибок, т.к. Ошибка выводится, но код продолжает выполняться в прежнем режиме
        """
        int(base[begin:end])
    except ValueError:
        print("Вероятно число введено неверно")

    if '+' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue

    elif '-' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue
    elif '/' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue
    elif '*' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue
    elif '(' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue
    elif ')' in base[begin:end+1]:
        # ЭТОТ БЛОК ИМЕЕТ СМЫСЛ ДОБАВИТЬ В ФУНКЦИЮ!
        operators.append(base[end])
        # добовление первого оператора в массив
        operands.append(int(base[begin:end]))
        # доблвление первого операнда
        # assert(operands[0] == 20), f"первый оператор определен неправильно, ожидалось 2, получено {operands[0]}"
        # проверка первого оператора
        begin = end+1
        end = end+2
        continue
    end = end + 1


print(operators)
print(operands)



"""
# функция выполнения математических операций
def calculating(operators, operands):

    for sign in operators:
        if sign == '*':
            operands[operators.index('*')] *= operands[operators.index('*')+1]
            del operands[operators.index('*')+1]
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


ans = calculating(operators, operands)
print(f"{base} = {ans}")
"""