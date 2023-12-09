import pyautogui 
import time
from time import sleep
'''
1. 检测机制，他是[x-->last]，x可以取截取的右侧，也可以是再右边一点（再右边的在他这个算法只是为了减少检测量），这个区间内发现颜色不同触发跳跃。直观点说就是一个探测器告诉你距离last-x的方位有障碍物，给一个缓冲时间来跳跃。
还有很多可以改进，既然是一个提醒作用，这个区间就可以缩小（甚至其实只需要一条竖线）因为实际有用的只是那两条线上的像素，更具体来说，是线上末端的一段（如果线选的比较好，只要比较末端），不需要从头到尾，也不需要平均，减少计算；
题外话：另一方面，其实取巧了，两条线上只有障碍物，没有云，如果碰到云了可能就难处理，其实还好，比如说只检测颜色，障碍物是黑色的，而云是灰色的。
2. 检测范围，如何选择last，目前还是基于测试；理想的话，如果可以获取速度的话，没有建立模型，但是至少直到速度和last是线性的，而不是现在阶梯的。
3. 两条线段：这个差不多有结论，龙的头部和尾巴那里。
4. 图像放缩，这个好像直接用原生的匹配的方法，无法解决。

相比较v1更自动化，、基于比例关系，所以up和down不太需要自己找了，同时不用每一个都设一个参数
'''

def run_game():
    while True:
        dinosaur = pyautogui.locateOnScreen('dinosaur.jpg', confidence=0.99)
        if dinosaur:
            break
    print(dinosaur)
    pyautogui.click(x=dinosaur.left - 80, y=dinosaur.top + 30)
    pyautogui.press('space')
    sleep(2)
    while True:
        dinosaur = pyautogui.locateOnScreen('head.jpg', confidence=0.5)
        if dinosaur:
            break
    print(dinosaur)
    # exit() 
    screenshot = pyautogui.screenshot('aa.jpg', region=(int(dinosaur[0]), int(dinosaur[1]), int(dinosaur.width * 5), int(dinosaur.height * 1.2))) # 450 80
    start_time = time.time()
    pyautogui.press("space")
    # 参数设置
    x = int(dinosaur.width * 2) #220  # 程序读取像素的起点，要比dinosaur的width大30个像素左右，我的是57，我x值取90
    y_up, y_down = int(dinosaur.height * 0.1), int(dinosaur.height * 0.9)
    pix_up, pix_down = [], []
    arr = range(0, int(dinosaur.width * 5 - x), 2)
    print(len(arr))
    last = 40 * 2
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
            last = 55 * 3
        elif 150 > (now_time - start_time) > 50:
            if not ck[1]:
                ck[1] = 3.5
                print('mode 2')
            pause_1, pause_2 = 0.3, 0.06
            last = 68 * 4
        elif 250 > (now_time - start_time) > 150:
            if not ck[2]:
                ck[2] = 1
                print('mode 3')
            pause_1, pause_2 = 0.25, 0.0
            last = 70 * 4
        elif 550 > (now_time - start_time) > 250:
            if not ck[3]:
                ck[3] = 1
                print('mode 4')
            last = 71 * 4
            pause_1, pause_2 = 0.25, 0.0
        elif (now_time - start_time) > 550:
            if not ck[4]:
                ck[4] = 1
                print('mode 5')
            last = 72 * 3.5
            pause_1, pause_2 = 0.2, 0.0  
        screenshot = pyautogui.screenshot(region=(int(dinosaur[0]), int(dinosaur[1]), int(dinosaur.width * 5), int(dinosaur.height * 1.2)))
        # exit()
        # pyautogui.screenshot('bb.jpg', region=(int(dinosaur[0] + x), int(dinosaur[1])+y_up, last * 2, y_down-y_up))
        # exit()
        for i in arr[:int(last)]:
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
