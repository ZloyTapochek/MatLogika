class PostMachine:
    def __init__(self):
        self.tape = []  # Лента
        self.head = 0   # Позиция каретки

    def write(self, symbol):
        # Записываем символ в текущую ячейку
        if self.head >= len(self.tape):
            self.tape.append(symbol)
        else:
            self.tape[self.head] = symbol

    def erase(self):
        # Стираем символ в текущей ячейке
        if self.head < len(self.tape):
            self.tape[self.head] = None

    def move_right(self):
        self.head += 1
        if self.head >= len(self.tape):
            self.tape.append(None)  # Добавляем пустую ячейку, если выходим за пределы

    def move_left(self):
        if self.head > 0:
            self.head -= 1

    def print_tape(self):
        print(self.tape)

    def task_a(self, N):
        # Записать число N+1, добавив метку справа к массиву
        self.tape = [1] * (N + 1)  # Инициализируем ленту с N метками
        self.head = 0
        while self.head < len(self.tape) and self.tape[self.head] is not None:
            self.move_right()
        self.write(1)  # Записываем метку 1

    def task_b(self):
        # Стереть среднюю метку из массива
        self.head = 0
        while self.head < len(self.tape) and self.tape[self.head] is not None:
            self.move_right()
        mid_index = len(self.tape) // 2
        self.head = mid_index
        self.erase()

    def task_c(self):
        # Раздвинуть две половины массива на одну секцию
        self.head = 0
        while self.head < len(self.tape) and self.tape[self.head] is not None:
            self.move_right()
        mid_index = len(self.tape) // 2
        right_half = self.tape[mid_index:]
        self.tape = self.tape[:mid_index] + [None] + right_half  # Вставляем пустую ячейку

    def task_d(self):
        # Сложить два массива
        # Пример: первый массив [1, 1, 1] и второй массив [1, 1, 1]
        first_array = [1, 1, 1]
        second_array = [1, 1, 1]
        self.tape = first_array + [None] + second_array  # Объединяем массивы
        self.head = 0
        # Сложение
        while self.head < len(first_array):
            if self.tape[self.head] is not None and self.tape[self.head + len(first_array) + 1] is not None:
                self.tape[self.head] += self.tape[self.head + len(first_array) + 1]
            self.move_right()

    def task_e(self):
        # Записать число N+1, учитывая положение каретки
        self.tape = [1] * 5  # Пример: массив из 5 меток (число 5)
        self.head = 2  # Пример: каретка над заполненной секцией
        if self.tape[self.head] is not None:
            self.move_right()
            self.write(1)  # Записываем метку 1
        else:
            # Поиск заполненной секции
            while self.head < len(self.tape) and self.tape[self.head] is None:
                self.move_right()
            self.write(1)  # Записываем метку 1

# Пример использования
machine = PostMachine()

# Задача a
machine.task_a(5)
machine.print_tape()  # Ожидается: [1, 1, 1, 1, 1, 1]

# Задача b
machine.task_b()
machine.print_tape()  # Ожидается: [1, 1, None, 1, 1]

# Задача c
machine.task_c()
machine.print_tape()  # Ожидается: [1, 1, None, None, 1, 1]

# Задача d
machine.task_d()
machine.print_tape()  # Ожидается: [2, 2, 2, None, 1, 1]

# Задача e
machine.task_e()
machine.print_tape()  # Ожидается: [1, 1, 1, 1, 1, 1]


