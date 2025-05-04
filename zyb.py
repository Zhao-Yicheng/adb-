from screen_control import ScreenControl
from time import sleep
# 初始化屏幕控制对象
screen = ScreenControl()

# 在屏幕下方绘制向下斜线
def h1():
    start_x = 500
    start_y = 2000
    end_x = 1200
    end_y = 2500
    screen.swipe(start_x, start_y, end_x, end_y,40)
def h2():
    start_x = 1200
    start_y = 2000
    end_x = 500
    end_y = 2500
    screen.swipe(start_x, start_y, end_x, end_y,40)
def a():
    for _ in range(10):
        h1()
        h2()
def b():
    screen.tap(1050,2550)
    sleep(7.5)
    a()

for i in range(10):
    b()
    sleep(1)