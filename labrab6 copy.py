def add_one_to_n(tape):
    """a) Запись числа N+1"""
    tape.append('1')  # Добавляем метку '1' справа
    return tape

def erase_middle(tape):
    """b) Стирание средней метки"""
    middle_index = len(tape) // 2
    del tape[middle_index]  # Удаляем среднюю метку
    return tape

def expand_array(tape):
    """c) Раздвижение двух половин массива"""
    mid_index = len(tape) // 2
    tape.insert(mid_index, '')  # Вставляем пустую метку в середину
    return tape

def add_arrays(tape1, tape2):
    """d) Сложение двух массивов"""
    return tape1 + tape2  # Склеиваем два массива

def add_one_with_cursor(tape, cursor_position):
    """e) Запись числа N+1 с произвольным положением каретки"""
    if cursor_position < len(tape) and tape[cursor_position] != '':
        # Каретка над заполненной секцией
        tape.append('1')  # Добавляем метку '1' справа
    else:
        # Каретка над пустой секцией, ищем массив
        for i in range(len(tape)):
            if tape[i] != '':
                tape.append('1')  # Добавляем метку '1' справа
                break
    return tape

def subtract_arrays(tape1, tape2):
    """Вычитание одного массива из другого"""
    # Проверяем, что оба массива не пустые
    if not tape1 or not tape2:
        return tape1  # Если один из массивов пустой, возвращаем уменьшаемое

    # Считаем количество '1' в каждом массиве
    count1 = tape1.count('1')
    count2 = tape2.count('1')

    # Если вычитаемое больше уменьшаемого, возвращаем пустой массив
    if count2 > count1:
        return []  # Или можно вернуть tape1, если хотите оставить уменьшаемое

    # Вычитаем количество '1' из tape1
    result_count = count1 - count2
    return ['1'] * result_count  # Возвращаем массив с разностью

def divide_array_by_two(tape):
    """Разделить заданное число на два"""
    count = tape.count('1')  # Считаем количество '1'
    result_count = count // 2  # Делим на два (округление вниз)
    return ['1'] * result_count  # Возвращаем массив с результатом

def multiply_array_by_three(tape):
    """Умножить заданное число на три"""
    count = tape.count('1')  # Считаем количество '1'
    result_count = count * 3  # Умножаем на три
    return ['1'] * result_count  # Возвращаем массив с результатом

# Примеры использования
if __name__ == "__main__":
    # Пример a
    tape_a = ['1', '1', '1']  # Представляет число 3
    result_a = add_one_to_n(tape_a)
    print("Результат a:", result_a)  # ['1', '1', '1', '1']

    # Пример b
    tape_b = ['1', '1', '1', '1', '1']  # 5 меток
    result_b = erase_middle(tape_b)
    print("Результат b:", result_b)  # ['1', '1', '1', '1']

    # Пример c
    tape_c = ['1', '1', '1', '1', '1', '1']  # 6 меток
    result_c = expand_array(tape_c)
    print("Результат c:", result_c)  # ['1', '1', '1', '', '1', '1', '1']

    # Пример d
    tape_d1 = ['1', '1', '1']  # 3 метки
    tape_d2 = ['1', '1']       # 2 метки
    result_d = add_arrays(tape_d1, tape_d2)
    print("Результат d:", result_d)  # ['1', '1', '1', '1', '1']

    # Пример e
    tape_e = ['1', '1', '1']  # Представляет число 3
    cursor_position = 3  # Каретка над пустой секцией
    result_e = add_one_with_cursor(tape_e, cursor_position)
    print("Результат e:", result_e)  # ['1', '1', '1', '1']

    # Пример вычитания
    tape_sub1 = ['1', '1', '1', '1']  # Уменьшаемое (4)
    tape_sub2 = ['1', '1']             # Вычитаемое (2)
    result_sub = subtract_arrays(tape_sub1, tape_sub2)
    print("Результат вычитания:", result_sub)  # ['1', '1']

    # Пример, когда вычитаемое больше уменьшаемого
    tape_sub3 = ['1', '1']              # Уменьшаемое (2)
    tape_sub4 = ['1', '1', '1']         # Вычитаемое (3)
    result_sub2 = subtract_arrays(tape_sub3, tape_sub4)
    print("Результат вычитания (вычитаемое больше):", result_sub2)  # []

    # Пример деления
    tape_div = ['1', '1', '1', '1']  # Представляет число 4
    result_div = divide_array_by_two(tape_div)
    print("Результат деления на два:", result_div)  # ['1', '1']

    # Пример деления с нечетным числом
    tape_div_odd = ['1', '1', '1']  # Представляет число 3
    result_div_odd = divide_array_by_two(tape_div_odd)
    print("Результат деления на два (нечетное число):", result_div_odd)  # ['1']

    # Пример умножения на три
    tape_mul = ['1', '1']  # Представляет число 2
    result_mul = multiply_array_by_three(tape_mul)
    print("Результат умножения на три:", result_mul)  # ['1', '1', '1', '1', '1', '1']

    # Пример умножения на три с нечетным числом
    tape_mul_odd = ['1', '1', '1']  # Представляет число 3
    result_mul_odd = multiply_array_by_three(tape_mul_odd)
    print("Результат умножения на три (нечетное число):", result_mul_odd)  # ['1', '1', '1', '1', '1', '1', '1', '1', '1']
