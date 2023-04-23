import keyboard as kb
import win32api as win

import functools
import time


# получить язык раскладки клавиатуры
def get_name_layout():
    name = win.GetKeyboardLayoutName()
    if name == '00000409':
        return 'en'
    elif name == '00000419':
        return 'ru'


# меняет раскладку клавиатуры
def change_layout(set_lay=None):
    if set_lay == 'ru' or set_lay == 'en':
        current_lay = get_name_layout()
        if current_lay == set_lay:
            pass
        else:
            kb.press_and_release('shift + alt')
    else:
        kb.press_and_release('shift + alt')

# функция вычисляющая время выполнения функции при помощи декоратора
def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper


@timer
def hello(times):
    count = 0
    for i in range(10 * times):
        count += 1
    return count
