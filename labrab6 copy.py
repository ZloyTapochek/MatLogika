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
