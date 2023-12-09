import pywt
import cv2
import numpy as np
# 设置融合的规则，平均、最小、最大
def fuseCoeff(cooef1, cooef2, method):
    if (method == 'mean'):
        cooef = (cooef1 + cooef2) / 2
    elif (method == 'min'):
        cooef = np.minimum(cooef1, cooef2)
    elif (method == 'max'):
        cooef = np.maximum(cooef1, cooef2)
    return cooef

# 设置参数
FUSION_METHOD = 'mean' 
FUSION_METHOD1 = 'max'
# 读取文件
I1 = cv2.imread('.\IR_meting003_g.bmp', 0)
I2 = cv2.imread('.\VIS_meting003_r.bmp', 0)
# 第一步：对每个图像进行小波变换，此处选用db2方法
wavelet = 'db2'
cooef1 = pywt.wavedec2(I1[:, :], wavelet, level=1)
cooef2 = pywt.wavedec2(I2[:, :], wavelet, level=1)
# 第二步：对于两幅图像中的每一尺度（要变换多少层），此处设置1层，根据设置的选项进行融合，
fusedCooef = []
for i in range(len(cooef1)):
    # 每个分解中的第一层的值采用平均法
    if (i == 0):
        fusedCooef.append(fuseCoeff(cooef1[0], cooef2[0], FUSION_METHOD))
    else:
        # 对于剩下的各层，各有3参数，采用最大法融合
        c1 = fuseCoeff(cooef1[i][0], cooef2[i][0], FUSION_METHOD1)
        c2 = fuseCoeff(cooef1[i][1], cooef2[i][1], FUSION_METHOD1)
        c3 = fuseCoeff(cooef1[i][2], cooef2[i][2], FUSION_METHOD1)
        fusedCooef.append((c1, c2, c3))
# 第三步：小波融合后，执行逆变换变成图像
fusedImage = pywt.waverec2(fusedCooef, wavelet)
# 第四步：归一化变成uint8格式
fusedImage1 = np.multiply(np.divide(fusedImage - np.min(fusedImage), (np.max(fusedImage) - np.min(fusedImage))), 255)
fusedImage1 = fusedImage1.astype(np.uint8)
# 第五步：输出图像
cv2.imwrite("win.bmp", fusedImage1)