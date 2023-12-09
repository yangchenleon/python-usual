import pyautogui as pg
import cv2

'''
和小恐龙无关，用cv2匹配图像并点击的过程
'''

def get_xy():
    pg.screenshot().save('screenshot.png')
    img = cv2.imread('screenshot.png')

    img_terminal = cv2.imread('icon.jpg')
    h, w, c = img_terminal.shape
    result = cv2.matchTemplate(img, img_terminal, cv2.TM_CCOEFF_NORMED)
    upper_left = cv2.minMaxLoc(result)[3]
    lower_right = (upper_left[0] + w, upper_left[1] + h)
    avg = (upper_left[0] + lower_right[0]) / 2, (upper_left[1] + lower_right[1]) / 2
    return avg

if __name__ == '__main__':
    pg.moveTo(get_xy())
    pg.click(get_xy())