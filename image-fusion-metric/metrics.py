import numpy as np
import math
import cv2


def ssim(img1, img2):
    # 常数项设置
    C1 = (0.01)**2
    C2 = (0.03)**2
    
    # 读取图像，设置滑动窗口
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    # 滑动窗口过滤，均值mu，标准差sigma，协方差sigma12
    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    # 带入公式求得ssim值
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()

# mse方法，直接带入公式
def mse(src, dst):
    return np.mean((src.astype(np.float64)-dst.astype(np.float64))**2)

# psnr方法，也是直接带入公式
def psnr(src, dst, Max = 255):
    mse_value = mse(src, dst)
    
    if mse_value == 0.:
        return np.inf
    return 10 * np.log10(Max**2 /mse_value)

#统计图像像素值——求统计直方图
def possible(img):
    tmp = [0] * 256
    k = 0

    for i in range(len(img)):
        for j in range(len(img[i])):
            # 找到像素灰度值
            val = int(img[i][j] * 255)
            # 对应灰度值计数+1
            tmp[val] = tmp[val] + 1
            # 统计全部像素数量
            k = k + 1
    for i in range(len(tmp)):
        tmp[i] = float(tmp[i] / k)  
    return tmp 

#计算交叉熵  
def cross_entropy(img1,img2):
    res = 0
    # 求直方图
    tmp1 = possible(img1) 
    tmp2 = possible(img2)           
    for i in range(len(tmp1)):
        if(tmp1[i] == 0 or tmp2[i] == 0):
            # 为0时无法做除法
            res = res
        else:
            # 带入公式
            res = float( res + tmp1[i] * (math.log(tmp1[i]/tmp2[i]) + tmp2[i] * (math.log(tmp2[i]/tmp1[i])))) 
    return res