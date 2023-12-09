# 导入相关模块，包括实现的那些评价方法
import numpy as np
import cv2
import matplotlib.pyplot as plt
from metrics import ssim, mse, psnr, cross_entropy

# 原始比较图片为可见光VIS图像_VIS_meting003_r.bmp
# 可替换为红外IR图像_IR_meting003_g.bmp进行比较
img = cv2.imread("VIS_meting003_r.bmp", 0) # 0表示以灰度图格式读取
img = img.astype('float') / 255.0 # 归一化处理
rows, cols = img.shape # 获得其尺寸

# 融合图像——采用哈尔小波
img_haar = cv2.imread("win.bmp", 0) # 0表示以灰度图格式读取
img_haar = img_haar.astype('float') / 255.0 # 归一化处理

# 融合图像——采用db2小波
img_db2 = cv2.imread("fusion.bmp", 0) # 0表示以灰度图格式读取
img_db2 = img_db2.astype('float') / 255.0 # 归一化处理

# 设置plot
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
                         sharex=True, sharey=True)
ax = axes.ravel()

# 原始图像和自己的评价指标的mse、ssim、psnr、CE的评价
mse_none = mse(img, img)
ssim_none = ssim(img, img)
psnr_none = psnr(img, img)
entropy_none = cross_entropy(img, img)

# 原始图像和采用哈尔小波的融合图像的评价指标的mse、ssim、psnr、CE的评价
mse_haar = mse(img, img_haar)
ssim_haar = ssim(img, img_haar)
psnr_haar = psnr(img, img_haar)
entropy_haar = cross_entropy(img, img_haar)

# 原始图像和采用db2小波的融合图像的评价指标的mse、ssim、psnr、CE的评价
mse_db2 = mse(img, img_db2)
ssim_db2 = ssim(img, img_db2)
psnr_db2 = psnr(img, img_db2)
entropy_db2 = cross_entropy(img, img_db2)

# 公共标签设置
label = 'MSE: {:.2f}, SSIM: {:.2f}\nPSNR: {:.2f}, EN: {:.2f}'

# 为每一个subplot现实图像，设置标题
ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(label.format(mse_none, ssim_none, psnr_none, entropy_none))
ax[0].set_title('Original image')

ax[1].imshow(img_haar, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(label.format(mse_haar, ssim_haar, psnr_haar, entropy_haar))
ax[1].set_title('Fused Image using haar wavelet')

ax[2].imshow(img_db2, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[2].set_xlabel(label.format(mse_db2, ssim_db2, psnr_db2, entropy_db2))
ax[2].set_title('Fused Image using db2 wavelet')

# 显示最后结果
plt.tight_layout()
plt.show()