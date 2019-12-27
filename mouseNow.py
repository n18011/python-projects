# マウスカーソルの現在位置を表示する

import pyautogui

print('中断するにはCtrl+Cを押してください')

try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\n終了')
