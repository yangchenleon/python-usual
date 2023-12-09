import pyautogui
import time
from time import sleep


def run_game():
    while True:
        dinosaur = pyautogui.locateOnScreen('dinosaur.jpg', confidence=0.99)
        if dinosaur:
            break
    print(dinosaur)
    pyautogui.click(dinosaur.left - 80, dinosaur.top + 30)
    screenshot = pyautogui.screenshot('aa.jpg', region=(int(dinosaur[0]), int(dinosaur[1]), 300, 80))
    start_time = time.time()
    pyautogui.press("space")
    # 参数设置
    x = 220  # 程序读取像素的起点，要比dinosaur的width大30个像素左右，我的是57，我x值取90
    y_up, y_down = 15, 55
    pix_up, pix_down = [], []
    arr = range(0, 360, 2)
    last = 40
    pause_1, pause_2 = 0.5, 0.15
    ck = [0,0,0,0,0]
    while True:
        pix_up.clear()
        pix_down.clear()
        now_time = time.time()
        if 50 > (now_time - start_time) > 30:
            if not ck[0]:
                ck[0] = 1
                print('mode 1')
            pause_1, pause_2 = 0.35, 0.08
            last = 55
        elif 150 > (now_time - start_time) > 50:
            if not ck[1]:
                ck[1] = 1
                print('mode 2')
            pause_1, pause_2 = 0.3, 0.0
            last = 68
        elif 250 > (now_time - start_time) > 150:
            if not ck[2]:
                ck[2] = 1
                print('mode 3')
            pause_1, pause_2 = 0.25, 0.0
            last = 70
        elif 550 > (now_time - start_time) > 250:
            if not ck[3]:
                ck[3] = 1
                print('mode 4')
            last = 71
            pause_1, pause_2 = 0.25, 0.0
        elif (now_time - start_time) > 550:
            if not ck[4]:
                ck[4] = 1
                print('mode 5')
            last = 72
            pause_1, pause_2 = 0.2, 0.0  
        screenshot = pyautogui.screenshot(region=(int(dinosaur[0]), int(dinosaur[1]), 450, 80))
        # exit()
        # pyautogui.screenshot('bb.jpg', region=(int(dinosaur[0] + x), int(dinosaur[1])+y_up, last * 2, y_down-y_up))
        # exit()
        for i in arr[:last]:
            # print(x + i, y_up)
            pix1 = screenshot.getpixel((x + i, y_up))
            pix2 = screenshot.getpixel((x + i, y_down))
            
            pix_up.append(pix1[0])
            pix_down.append(pix2[0])

        if pix_down[0] != sum(pix_down) / len(pix_down):
            pyautogui.keyDown("space", _pause=False)
            sleep(pause_2)
            pyautogui.keyUp("space", _pause=False)
        
        elif pix_up[0] != sum(pix_up) / len(pix_up):  
            pyautogui.keyDown("down", _pause=False) 
            sleep(pause_1)
            pyautogui.keyUp("down", _pause=False)
        


if __name__ == '__main__':
    run_game()
