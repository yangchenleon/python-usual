# 导入相关模块，包括实现的那些评价方法
import numpy as np
import cv2
import matplotlib.pyplot as plt
from metrics import ssim, mse, psnr, cross_entropy
# from skimage.metrics import structural_similarity as ssim
# from skimage.metrics import mean_squared_error as mse

img = cv2.imread("a.jpg") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# chrows, cols = img.shape # 获得其尺寸

# 融合图像——采用哈尔小波
img_haar = cv2.imread("b.jpg")
img_haar = cv2.cvtColor(img_haar, cv2.COLOR_BGR2RGB)

# 设置plot
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                         sharex=True, sharey=True)
ax = axes.ravel()

# 原始图像和自己的评价指标的mse、ssim、psnr、CE的评价
# mse_none = mse(img, img)
ssim_none = ssim(img, img)
psnr_none = psnr(img, img)

# 原始图像和采用哈尔小波的融合图像的评价指标的mse、ssim、psnr、CE的评价
# mse_haar = mse(img, img_haar)
ssim_haar = ssim(img, img_haar)
psnr_haar = psnr(img, img_haar)

# 公共标签设置
label = 'SSIM: {:.2f}\nPSNR: {:.2f}'

# 为每一个subplot现实图像，设置标题
ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(label.format(ssim_none, psnr_none))
ax[0].set_title('ground truth')

ax[1].imshow(img_haar, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(label.format(ssim_haar, psnr_haar))
ax[1].set_title('inpainted image')

# 显示最后结果
plt.tight_layout()
plt.show()