import win32gui
from time import sleep
import os

window_name = None
path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(path, 'window-name.txt'), encoding='utf-8') as f:
    window_name = f.readline()


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    text = win32gui.GetWindowText(hwnd)

    if window_name in text:
        print(f'x:{x}\ny:{y}')
        print(f'width: {w}\ntheight:{h}')


if __name__ == '__main__':
    while True:
        win32gui.EnumWindows(callback, None)
        sleep(0.5)
        os.system('cls')
