from tkinter import Tk, Canvas, Label
import keyboard


class MyWindow:
    def __init__(self, width, height):
        # Ширина и высота окна
        self.window_width = width
        self.window_height = height

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

        # 'key': [x0, y0, x1, y1, ряд, счет нажатий]
        self.keys_dict = {
            'esc': [2, 2, 27, 27, '0', 0],
            'f1': [29, 2, 54, 27, '0', 0],
            'f2': [56, 2, 81, 27, '0', 0],
            'f3': [83, 2, 108, 27, '0', 0],
            'f4': [110, 2, 135, 27, '0', 0],
            'f5': [137, 2, 162, 27, '0', 0],
            'f6': [164, 2, 189, 27, '0', 0],
            'f7': [191, 2, 216, 27, '0', 0],
            'f8': [218, 2, 243, 27, '0', 0],
            'f9': [245, 2, 270, 27, '0', 0],
            'f10': [272, 2, 297, 27, '0', 0],
            'f11': [299, 2, 324, 27, '0', 0],
            'f12': [326, 2, 351, 27, '0', 0],
            'print screen': [353, 2, 378, 27, '0', 0],
            'pause': [380, 2, 405, 27, '0', 0],
            'insert': [407, 2, 432, 27, '0', 0],
            'delete': [434, 2, 459, 27, '0', 0],

            '`': [2, 2, 17, 32, '1', 0],
            '1': [19, 2, 49, 32, '1', 0],
            '2': [51, 2, 81, 32, '1', 0],
            '3': [83, 2, 113, 32, '1', 0],
            '4': [115, 2, 145, 32, '1', 0],
            '5': [147, 2, 177, 32, '1', 0],
            '6': [179, 2, 209, 32, '1', 0],
            '7': [211, 2, 241, 32, '1', 0],
            '8': [243, 2, 273, 32, '1', 0],
            '9': [275, 2, 305, 32, '1', 0],
            '0': [307, 2, 337, 32, '1', 0],
            '-': [339, 2, 369, 32, '1', 0],
            '=': [371, 2, 401, 32, '1', 0],
            'backspace': [403, 2, 463, 32, '1', 0],

            'tab': [2, 32, 40, 62, '2', 0],
            'q': [42, 32, 72, 62, '2', 0],
            'w': [74, 32, 104, 62, '2', 0],
            'e': [106, 32, 136, 62, '2', 0],
            'r': [138, 32, 168, 62, '2', 0],
            't': [170, 32, 200, 62, '2', 0],
            'y': [202, 32, 232, 62, '2', 0],
            'u': [234, 32, 264, 62, '2', 0],
            'i': [266, 32, 296, 62, '2', 0],
            'o': [298, 32, 328, 62, '2', 0],
            'p': [330, 32, 360, 62, '2', 0],
            '[': [362, 32, 392, 62, '2', 0],
            ']': [394, 32, 424, 62, '2', 0],
            '\\': [426, 32, 471, 62, '2', 0],

            'caps lock': [2, 32, 46, 62, '3', 0],
            'a': [48, 32, 78, 62, '3', 0],
            's': [80, 32, 110, 62, '3', 0],
            'd': [112, 32, 142, 62, '3', 0],
            'f': [144, 32, 174, 62, '3', 0],
            'g': [176, 32, 206, 62, '3', 0],
            'h': [208, 32, 238, 62, '3', 0],
            'j': [240, 32, 270, 62, '3', 0],
            'k': [272, 32, 302, 62, '3', 0],
            'l': [304, 32, 334, 62, '3', 0],
            ';': [336, 32, 366, 62, '3', 0],
            "'": [368, 32, 398, 62, '3', 0],
            'enter': [400, 32, 464, 62, '3', 0],

            'shift': [2, 64, 46, 94, '4', 0],
            'z': [48, 64, 78, 94, '4', 0],
            'x': [80, 64, 110, 94, '4', 0],
            'c': [112, 64, 142, 94, '4', 0],
            'v': [144, 64, 174, 94, '4', 0],
            'b': [176, 64, 206, 94, '4', 0],
            'n': [208, 64, 238, 94, '4', 0],
            'm': [240, 64, 270, 94, '4', 0],
            ',': [272, 64, 302, 94, '4', 0],
            '.': [304, 64, 334, 94, '4', 0],
            '/': [336, 64, 366, 94, '4', 0],
            'right shift': [368, 64, 470, 94, '4', 0],

            'ctrl': [2, 96, 32, 126, '5', 0],
            'fn': [34, 96, 64, 126, '5', 0],
            'left windows': [66, 96, 96, 126, '5', 0],
            'alt': [98, 96, 128, 126, '5', 0],
            'space': [130, 96, 240, 126, '5', 0],
            'right alt': [242, 96, 272, 126, '5', 0],
            'menu': [274, 96, 304, 126, '5', 0],
            'right ctrl': [306, 96, 336, 126, '5', 0],
            'left': [338, 96, 368, 126, '5', 0],
            'up': [370, 96, 400, 126, '5', 0],
            'down': [402, 96, 432, 126, '5', 0],
            'right': [434, 96, 464, 126, '5', 0]
        }

        self.key_color = 'lightgray'
        self.key_border_color = 'gray'
        self.key_pressed_color = 'gray'
        self.key_pressed_border_color = 'red'

        self.keys_indent = 2  # отступ клавиш

        self.keys_canvas_dict = {}  # словарь объектов отрисовки клавиш
        self.keys_list = list(self.keys_dict)  # список клавиш
        self.values_list = list(self.keys_dict.values())  # список координат клавиш

        # Список координат клавиш по рядам
        self.keys_coord_list = [[], [], [], [], [], []]
        for i in range(len(self.values_list)):
            values = self.values_list[i]
            self.keys_coord_list[int(self.values_list[i][4])].append([values[0], values[1], values[2], values[3]])

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

        self.label_esc = Label(self.root, text='esc', bg=self.key_color)
        self.label_f1 = Label(self.root, text='f1', bg=self.key_color)
        self.label_f2 = Label(self.root, text='f2', bg=self.key_color)
        self.label_f3 = Label(self.root, text='f3', bg=self.key_color)
        self.label_f4 = Label(self.root, text='f4', bg=self.key_color)
        self.label_f5 = Label(self.root, text='f5', bg=self.key_color)
        self.label_f6 = Label(self.root, text='f6', bg=self.key_color)
        self.label_f7 = Label(self.root, text='f7', bg=self.key_color)
        self.label_f8 = Label(self.root, text='f8', bg=self.key_color)
        self.label_f9 = Label(self.root, text='f9', bg=self.key_color)
        self.label_f10 = Label(self.root, text='f10', bg=self.key_color)
        self.label_f11 = Label(self.root, text='f11', bg=self.key_color)
        self.label_f12 = Label(self.root, text='f12', bg=self.key_color)
        self.label_print_screen = Label(self.root, text='print\nscreen', bg=self.key_color)
        self.label_pause = Label(self.root, text='pause', bg=self.key_color)
        self.label_insert = Label(self.root, text='insert', bg=self.key_color)
        self.label_delete = Label(self.root, text='delete', bg=self.key_color)
        self.label_tilde = Label(self.root, text='`', bg=self.key_color)
        self.label_1 = Label(self.root, text='1', bg=self.key_color)
        self.label_2 = Label(self.root, text='2', bg=self.key_color)
        self.label_3 = Label(self.root, text='3', bg=self.key_color)
        self.label_4 = Label(self.root, text='4', bg=self.key_color)
        self.label_5 = Label(self.root, text='5', bg=self.key_color)
        self.label_6 = Label(self.root, text='6', bg=self.key_color)
        self.label_7 = Label(self.root, text='7', bg=self.key_color)
        self.label_8 = Label(self.root, text='8', bg=self.key_color)
        self.label_9 = Label(self.root, text='9', bg=self.key_color)
        self.label_0 = Label(self.root, text='0', bg=self.key_color)
        self.label_minus = Label(self.root, text='-', bg=self.key_color)
        self.label_equal = Label(self.root, text='=', bg=self.key_color)
        self.label_backspace = Label(self.root, text='backspace', bg=self.key_color)
        self.label_tab = Label(self.root, text='tab', bg=self.key_color)
        self.label_q = Label(self.root, text='q', bg=self.key_color)
        self.label_w = Label(self.root, text='w', bg=self.key_color)
        self.label_e = Label(self.root, text='e', bg=self.key_color)
        self.label_r = Label(self.root, text='r', bg=self.key_color)
        self.label_t = Label(self.root, text='t', bg=self.key_color)
        self.label_y = Label(self.root, text='y', bg=self.key_color)
        self.label_u = Label(self.root, text='u', bg=self.key_color)
        self.label_i = Label(self.root, text='i', bg=self.key_color)
        self.label_o = Label(self.root, text='o', bg=self.key_color)
        self.label_p = Label(self.root, text='p', bg=self.key_color)
        self.label_op_scq_br = Label(self.root, text='[', bg=self.key_color)
        self.label_cl_scq_br = Label(self.root, text=']', bg=self.key_color)
        self.label_slash = Label(self.root, text='\\', bg=self.key_color)
        self.label_caps_lock = Label(self.root, text='caps\nlock', bg=self.key_color)
        self.label_a = Label(self.root, text='a', bg=self.key_color)
        self.label_s = Label(self.root, text='s', bg=self.key_color)
        self.label_d = Label(self.root, text='d', bg=self.key_color)
        self.label_f = Label(self.root, text='f', bg=self.key_color)
        self.label_g = Label(self.root, text='g', bg=self.key_color)
        self.label_h = Label(self.root, text='h', bg=self.key_color)
        self.label_j = Label(self.root, text='j', bg=self.key_color)
        self.label_k = Label(self.root, text='k', bg=self.key_color)
        self.label_l = Label(self.root, text='l', bg=self.key_color)
        self.label_semicolon = Label(self.root, text=';', bg=self.key_color)
        self.label_apostrophe = Label(self.root, text="'", bg=self.key_color)
        self.label_enter = Label(self.root, text='enter', bg=self.key_color)
        self.label_shift = Label(self.root, text='shift', bg=self.key_color)
        self.label_z = Label(self.root, text='z', bg=self.key_color)
        self.label_x = Label(self.root, text='x', bg=self.key_color)
        self.label_c = Label(self.root, text='c', bg=self.key_color)
        self.label_v = Label(self.root, text='v', bg=self.key_color)
        self.label_b = Label(self.root, text='b', bg=self.key_color)
        self.label_n = Label(self.root, text='n', bg=self.key_color)
        self.label_m = Label(self.root, text='m', bg=self.key_color)
        self.label_comma = Label(self.root, text=',', bg=self.key_color)
        self.label_dot = Label(self.root, text='.', bg=self.key_color)
        self.label_slash_f = Label(self.root, text='/', bg=self.key_color)
        self.label_right_shift = Label(self.root, text='shift', bg=self.key_color)
        self.label_ctrl = Label(self.root, text='ctrl', bg=self.key_color)
        self.label_fn = Label(self.root, text='fn', bg=self.key_color)
        self.label_left_windows = Label(self.root, text='win', bg=self.key_color)
        self.label_alt = Label(self.root, text='alt', bg=self.key_color)
        self.label_space = Label(self.root, text='space', bg=self.key_color)
        self.label_right_alt = Label(self.root, text='alt', bg=self.key_color)
        self.label_menu = Label(self.root, text='menu', bg=self.key_color)
        self.label_right_ctrl = Label(self.root, text='ctrl', bg=self.key_color)
        self.label_left = Label(self.root, text='left', bg=self.key_color)
        self.label_up = Label(self.root, text='up', bg=self.key_color)
        self.label_down = Label(self.root, text='down', bg=self.key_color)
        self.label_right = Label(self.root, text='right', bg=self.key_color)

        self.label_dict = {'esc': self.label_esc,
                           'f1': self.label_f1,
                           'f2': self.label_f2,
                           'f3': self.label_f3,
                           'f4': self.label_f4,
                           'f5': self.label_f5,
                           'f6': self.label_f6,
                           'f7': self.label_f7,
                           'f8': self.label_f8,
                           'f9': self.label_f9,
                           'f10': self.label_f10,
                           'f11': self.label_f11,
                           'f12': self.label_f12,
                           'print screen': self.label_print_screen,
                           'pause': self.label_pause,
                           'insert': self.label_insert,
                           'delete': self.label_delete,
                           '`': self.label_tilde,
                           '1': self.label_1,
                           '2': self.label_2,
                           '3': self.label_3,
                           '4': self.label_4,
                           '5': self.label_5,
                           '6': self.label_6,
                           '7': self.label_7,
                           '8': self.label_8,
                           '9': self.label_9,
                           '0': self.label_0,
                           '-': self.label_minus,
                           '=': self.label_equal,
                           'backspace': self.label_backspace,
                           'tab': self.label_tab,
                           'q': self.label_q,
                           'w': self.label_w,
                           'e': self.label_e,
                           'r': self.label_r,
                           't': self.label_t,
                           'y': self.label_y,
                           'u': self.label_u,
                           'i': self.label_i,
                           'o': self.label_o,
                           'p': self.label_p,
                           '[': self.label_op_scq_br,
                           ']': self.label_cl_scq_br,
                           '\\': self.label_slash,
                           'caps lock': self.label_caps_lock,
                           'a': self.label_a,
                           's': self.label_s,
                           'd': self.label_d,
                           'f': self.label_f,
                           'g': self.label_g,
                           'h': self.label_h,
                           'j': self.label_j,
                           'k': self.label_k,
                           'l': self.label_l,
                           ';': self.label_semicolon,
                           "'": self.label_apostrophe,
                           'enter': self.label_enter,
                           'shift': self.label_shift,
                           'z': self.label_z,
                           'x': self.label_x,
                           'c': self.label_c,
                           'v': self.label_v,
                           'b': self.label_b,
                           'n': self.label_n,
                           'm': self.label_m,
                           ',': self.label_comma,
                           '.': self.label_dot,
                           '/': self.label_slash_f,
                           'right shift': self.label_right_shift,
                           'ctrl': self.label_ctrl,
                           'fn': self.label_fn,
                           'left windows': self.label_left_windows,
                           'alt': self.label_alt,
                           'space': self.label_space,
                           'right alt': self.label_right_alt,
                           'menu': self.label_menu,
                           'right ctrl': self.label_right_ctrl,
                           'left': self.label_left,
                           'up': self.label_up,
                           'down': self.label_down,
                           'right': self.label_right}
        self.label_list = list(self.label_dict)

        print(f'keys_list:  {self.keys_list}')
        print(f'label_list: {self.label_list}')

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
                self.canvas.itemconfig(key_item,
                                       fill=self.key_pressed_color,
                                       outline=self.key_pressed_border_color)

            if e.event_type == 'up':
                if key == 'esc':
                    self.root.quit()

                # меняем фон клавиш
                self.canvas.itemconfig(key_item,
                                       fill=self.key_color,
                                       outline=self.key_border_color)
                self.keys_dict[key][5] += 1

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
        keys_height = (self.window_height - ((self.keys_indent * row_count) + self.keys_indent)) / row_count

        # координаты первой клавиши
        x0 = 2
        x1 = (x0 + row_keys_width_total[1] * self.row_keys_width_weight[1][0])
        y0 = 0
        y1 = 0

        row = -1  # значение '-1' для того, чтобы первая итерация переходила в блок 'else'
        count = 0  # для получения индекса клавиши

        # Цикл для отрисовки последующих клавиш
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
                        y1 = (y0 + keys_height)

                    # Меняем координаты соответствующей клавише
                    self.canvas.coords(self.keys_canvas_dict[f'{self.keys_list[count]}'],
                                       x0, y0, x1, y1)

                    # Меняем координаты названия соответствующей клавиши
                    self.label_dict[self.label_list[count]].place(
                        x=x0+4,
                        y=y0+4,
                        width=x1-x0-7,
                        height=keys_height-7
                    )

                    count += 1

        for i in range(count):
            self.label_dict[self.label_list[i]].update_idletasks()

        # self.label_KEY_NAME.place(x=x0, y=y0, width=x1, height=y1)
        # self.label_KEY_NAME.update_idletasks()

    # Отрисовываем клавиши
    def draw_keys(self):
        min_x1 = 0
        min_y1 = 0

        # Проходимся по словарю self.keys_dict
        for i in range(len(self.keys_dict)):
            coord = self.keys_dict[f'{self.keys_list[i]}']  # получаем координаты ключа

            # Отрисовываем клавишу и присваиваем ей ключ в словаре
            self.keys_canvas_dict[f'{self.keys_list[i]}'] = self.canvas.create_rectangle(
                coord[0], coord[1], coord[2], coord[3],
                fill='lightgray', outline='gray'
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
