from tkinter import Tk, Canvas
import keyboard


class MyWindow:
    def __init__(self, width, height):
        # Ширина и высота окна
        self.window_width = width
        self.window_height = height

        # Создаем окно
        self.root = Tk()

        self.root.title('test3.py')  # название окна
        self.root.overrideredirect(False)  # отключить кнопки окна (свернуть, на весь экран, закрыть)

        # Задаем параметры геометрии окна (ширина, высота, расположение)
        self.root.geometry(str(self.window_width) + 'x' + str(self.window_height))

        # Регистрируем (bind) изменение параметров окна
        self.root.bind('<Configure>', self.window_resize)

        # Параметры холста
        self.canvas = Canvas(self.root,
                             width=self.window_width,
                             height=self.window_height,
                             bg='lightgray'
                             )
        self.canvas.pack()

        # Количество прямоугольников в ширину (x) и высоту (y)
        self.n_x = 3
        self.n_y = 3

        # Словарь прямоугольников (как объектов) и словарь их координатов
        self.rectangles_dict = {}
        self.rect_coord_dict = {}

        # 'key': [x0, y0, x1, y1, ряд]
        self.keys_coord_dict = {
            'esc': [2, 2, 27, 27, '0'],
            'f1': [29, 2, 54, 27, '0'],
            'f2': [56, 2, 81, 27, '0'],
            'f3': [83, 2, 108, 27, '0'],
            'f4': [110, 2, 135, 27, '0'],
            'f5': [137, 2, 162, 27, '0'],
            'f6': [164, 2, 189, 27, '0'],
            'f7': [191, 2, 216, 27, '0'],
            'f8': [218, 2, 243, 27, '0'],
            'f9': [245, 2, 270, 27, '0'],
            'f10': [272, 2, 297, 27, '0'],
            'f11': [299, 2, 324, 27, '0'],
            'f12': [326, 2, 351, 27, '0'],
            'print screen': [353, 2, 378, 27, '0'],
            'pause': [380, 2, 405, 27, '0'],
            'insert': [407, 2, 432, 27, '0'],
            'delete': [434, 2, 459, 27, '0'],

            '`': [2, 2, 17, 32, '1'],
            '1': [19, 2, 49, 32, '1'],
            '2': [51, 2, 81, 32, '1'],
            '3': [83, 2, 113, 32, '1'],
            '4': [115, 2, 145, 32, '1'],
            '5': [147, 2, 177, 32, '1'],
            '6': [179, 2, 209, 32, '1'],
            '7': [211, 2, 241, 32, '1'],
            '8': [243, 2, 273, 32, '1'],
            '9': [275, 2, 305, 32, '1'],
            '0': [307, 2, 337, 32, '1'],
            '-': [339, 2, 369, 32, '1'],
            '=': [371, 2, 401, 32, '1'],
            'backspace': [403, 2, 463, 32, '1'],

            'tab': [2, 32, 40, 62, '2'],
            'q': [42, 32, 72, 62, '2'],
            'w': [74, 32, 104, 62, '2'],
            'e': [106, 32, 136, 62, '2'],
            'r': [138, 32, 168, 62, '2'],
            't': [170, 32, 200, 62, '2'],
            'y': [202, 32, 232, 62, '2'],
            'u': [234, 32, 264, 62, '2'],
            'i': [266, 32, 296, 62, '2'],
            'o': [298, 32, 328, 62, '2'],
            'p': [330, 32, 360, 62, '2'],
            '[': [362, 32, 392, 62, '2'],
            ']': [394, 32, 424, 62, '2'],
            '\\': [426, 32, 471, 62, '2'],

            'caps lock': [2, 32, 46, 62, '3'],
            'a': [48, 32, 78, 62, '3'],
            's': [80, 32, 110, 62, '3'],
            'd': [112, 32, 142, 62, '3'],
            'f': [144, 32, 174, 62, '3'],
            'g': [176, 32, 206, 62, '3'],
            'h': [208, 32, 238, 62, '3'],
            'j': [240, 32, 270, 62, '3'],
            'k': [272, 32, 302, 62, '3'],
            'l': [304, 32, 334, 62, '3'],
            ';': [336, 32, 366, 62, '3'],
            "'": [368, 32, 398, 62, '3'],
            'enter': [400, 32, 464, 62, '3'],

            'shift': [2, 64, 46, 94, '4'],
            'z': [48, 64, 78, 94, '4'],
            'x': [80, 64, 110, 94, '4'],
            'c': [112, 64, 142, 94, '4'],
            'v': [144, 64, 174, 94, '4'],
            'b': [176, 64, 206, 94, '4'],
            'n': [208, 64, 238, 94, '4'],
            'm': [240, 64, 270, 94, '4'],
            ',': [272, 64, 302, 94, '4'],
            '.': [304, 64, 334, 94, '4'],
            '/': [336, 64, 366, 94, '4'],
            'right shift': [368, 64, 470, 94, '4'],

            'ctrl': [2, 96, 32, 126, '5'],
            'fn': [34, 96, 64, 126, '5'],
            'left windows': [66, 96, 96, 126, '5'],
            'alt': [98, 96, 128, 126, '5'],
            'space': [130, 96, 240, 126, '5'],
            'right alt': [242, 96, 272, 126, '5'],
            'menu': [274, 96, 304, 126, '5'],
            'right ctrl': [306, 96, 336, 126, '5'],
            'left': [338, 96, 368, 126, '5'],
            'up': [370, 96, 400, 126, '5'],
            'down': [402, 96, 432, 126, '5'],
            'right': [434, 96, 464, 126, '5']
            }

        self.keys_score_dict = {}
        self.keys_canvas_dict = {}
        self.keys_list = list(self.keys_coord_dict)
        self.values_list = list(self.keys_coord_dict.values())

        # Список координат клавиш по рядам
        self.keys_coord_list = [[], [], [], [], [], []]
        for i in range(len(self.values_list)):
            values = self.values_list[i]
            self.keys_coord_list[int(self.values_list[i][4])].append([values[0], values[1], values[2], values[3]])

        self.keys_indent = 2  # отступ клавиш

        # Список ширины клавиш по рядам
        self.row_keys_width = [[], [], [], [], [], []]
        for i in range(len(self.keys_coord_list)):
            for j in range(len(self.keys_coord_list[i])):
                if self.keys_coord_list[i]:
                    self.row_keys_width[i].append(self.keys_coord_list[i][j][2] - self.keys_coord_list[i][j][0])
                else:
                    continue

        # Список весов клавиш по рядам
        self.row_keys_width_weight = [[], [], [], [], [], []]
        for i in range(len(self.keys_coord_list)):
            for j in range(len(self.keys_coord_list[i])):
                if self.keys_coord_list[i]:
                    self.row_keys_width_weight[i].append(self.row_keys_width[i][j] / sum(self.row_keys_width[i]))
                else:
                    continue

        self.window_width_const = self.window_width
        self.window_height_const = self.window_height

        self.draw_keys()

        self.keyboard_activate()

        # Запускаем окно
        self.root.mainloop()

    # Активируем отслеживание клавиш
    def keyboard_activate(self):
        keyboard.hook(self.hook_pressed_keys)

    # когда отпустили клавишу прибавляем единицу к счету нажатия
    def hook_pressed_keys(self, e):
        key = str(e.name).lower()
        try:
            key_item = self.keys_canvas_dict[key]

            if e.event_type == 'down':
                # меняем фон клавиш
                self.canvas.itemconfig(key_item, fill='gray', outline='red')

            if e.event_type == 'up':
                # меняем фон клавиш
                self.canvas.itemconfig(key_item, fill='black', outline='lightgray')

        except:
            print(f'Такой клавиши нет: {key}')

    # Перерисовываем клавиши
    def redraw_keys(self):
        # Сумма ширины клавиш в ряду
        row_keys_width_total = []
        for i in range(len(self.row_keys_width)):
            if self.row_keys_width[i]:
                row_keys_width_total.append(self.window_width - (self.keys_indent *
                                                                      len(self.keys_coord_list[i]) + self.keys_indent))
            else:
                row_keys_width_total.append(1)

        # Сумма высоты клавиш
        row_count = 0
        for i in range(len(self.keys_coord_list)):
            if self.keys_coord_list[i]:
                row_count += 1
        row_keys_height_total = self.window_height - (self.keys_indent * row_count) + self.keys_indent

        x0 = 2
        x1 = (x0 + row_keys_width_total[1] * self.row_keys_width_weight[1][0])

        y0 = 0
        y1 = 0

        row = -1
        count = 0

        # Цикл для отрисовки последующий клавиш
        for i in range(len(self.keys_coord_list)):
            for j in range(len(self.keys_coord_list[i])):
                if self.keys_coord_list[i]:
                    if row == i:
                        # +2 к координате правой стороны предыдущей клавиши (отступ клавиши)
                        x0 = (x1 + self.keys_indent)
                        # задаем новую ширину соответствующей клавише
                        x1 = (x0 + row_keys_width_total[i] * self.row_keys_width_weight[i][j])

                    else:
                        row = i
                        # x0 первой клавиши ряда
                        x0 = self.keys_coord_list[i][j][0]
                        # измененное x1 первой клавиши ряда
                        x1 = (x0 + row_keys_width_total[i] * self.row_keys_width_weight[i][j])

                        y0 = y1 + 2
                        y1 = (y0 + row_keys_height_total / row_count)

                    # Меняем координаты соответствующей клавише
                    self.canvas.coords(self.keys_canvas_dict[f'{self.keys_list[count]}'],
                                       x0, y0, x1, y1)

                    count += 1

    # Отрисовываем клавиши
    def draw_keys(self):
        min_x1 = 0
        min_y1 = 0

        # Проходимся по словарю self.keys_dict
        for i in range(len(self.keys_coord_dict)):
            coord = self.keys_coord_dict[f'{self.keys_list[i]}']  # получаем координаты ключа

            # Отрисовываем клавишу и присваиваем ей ключ в словаре
            self.keys_canvas_dict[f'{self.keys_list[i]}'] = self.canvas.create_rectangle(
                coord[0], coord[1], coord[2], coord[3],
                fill='black', outline='lightgray'
            )

            # x0, y0, x1, y1
            if coord[2] > min_x1:
                min_x1 = coord[2]
            if coord[3] > min_y1:
                min_y1 = coord[3]

        self.root.geometry(f'{min_x1 + 2}x{min_y1 + 2}')
        print(f'{min_x1 + 2}x{min_y1 + 2}')

    # Отслеживание размера окна
    def window_resize(self, event=None):
        # Прослушиваем все события окна
        if event is not None:
            # Если заданный параметр ширины и высоты окна не соответствует новому
            if self.window_width != self.root.winfo_width() or \
                    self.window_height != self.root.winfo_height():

                if self.window_width != self.root.winfo_width():
                    self.window_width = self.root.winfo_width()  # Ширина
                    self.canvas.configure(width=self.window_width)

                    self.redraw_keys()

                if self.window_height != self.root.winfo_height():
                    self.window_height = self.root.winfo_height()  # Высота
                    self.canvas.configure(height=self.window_height)

                    self.redraw_keys()


width = 100
height = 100

win = MyWindow(width, height)
