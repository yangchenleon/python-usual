import pyautogui as pg
import time
'''
废了，无法绕过UAC
'''

print(pg.position())
pg.press('win')
pg.press('capslock')
pg.typewrite('caps', interval=0.1)

time.sleep(2)
print('enter1')
pg.press('enter')
time.sleep(2)
# print('left')
# pg.press('left')
# time.sleep(2)
# print('enter1')
# pg.press('enter')

pg.moveTo(100, 100, duration=0.25)
# pg.click(x=973, y=921, button='left', duration=0.25)

pg.hotkey('alt', 'y')
print('enter2')
pg.press('capslock')