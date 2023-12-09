import pyautogui as pg

# 1. 移动 & 点击
pg.moveTo(100, 100, duration=0.25)
pg.click(button='left', clicks=2, interval=0.25, duration=0.25)

# 2. 拖拽
pg.dragTo(100, 100, duration=0.25)

# 3. 持续动作（拖拽）
pg.mouseDown(button='left', x=100, y=100)
pg.moveTo(200, 200, duration=0.25)
pg.mouseUp(button='left', x=200, y=200)

# 4. 滚轮
pg.scroll(200)
pg.scroll(-900)

# 5. 键盘
pg.moveTo(100, 100, duration=0.25)
pg.click(button='left', clicks=2, interval=0.25, duration=0.25)
pg.typewrite('Hello World!', interval=0.1)

# 6. 按键
pg.press('hhhh')
pg.keyDown('enter')
pg.keyUp('enter')
pg.hotkey('ctrl', 'c') # equal to pg.keyDown('ctrl'); pg.keyDown('c'); pg.keyUp('c'); pg.keyUp('ctrl')

# 7. 截图
pg.screenshot('screenshot.png', region=(0, 0, 300, 400))

# 8. 获取坐标
button_location = pg.locateOnScreen('button.png', confidence=0.9)
print(button_location)
button_center = pg.center(button_location)
pg.moveTo(button_center, duration=0.25)
