# 导入相关模块，包括实现的那些评价方法
import numpy as np
import matplotlib.pyplot as plt
from metrics import ssim, mse, psnr, cross_entropy

from skimage import data, img_as_float
# 下为skimage模块现成的metric，选用
# from skimage.metrics import structural_similarity as ssim
# from skimage.metrics import mean_squared_error as mse

# 经典摄影师图片，获得其尺寸
img = img_as_float(data.camera())
rows, cols = img.shape

# 设置噪声
noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
noise[np.random.random(size=noise.shape) > 0.5] *= -1

# 一个是直接添加噪声，有正负噪声，另一个就是加正数，图像偏白，最后归一化
img_noise = (img + noise) / (1+abs(noise))
img_const = (img + abs(noise)) / (1+abs(noise))

# 设置plot
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
                         sharex=True, sharey=True)
ax = axes.ravel()

# 下面三组分别是对原始、噪声、正常数的mse、ssim、psnr、CE的评价
# ssim_none = ssim(img, img, data_range=img.max() - img.min())
mse_none = mse(img, img)
ssim_none = ssim(img, img)
psnr_none = psnr(img, img)
entropy_none = cross_entropy(img, img)

# ssim_noise = ssim(img, img_noise, data_range=img_noise.max() - img_noise.min())
mse_noise = mse(img, img_noise)
ssim_noise = ssim(img, img_noise)
psnr_noise = psnr(img, img_noise)
entropy_noise = cross_entropy(img, img_noise)

# ssim_const = ssim(img, img_const, data_range=img_const.max() - img_const.min())
mse_const = mse(img, img_const)
ssim_const = ssim(img, img_const)
psnr_const = psnr(img, img_const)
entropy_const = cross_entropy(img, img_const)

# 公共标签设置
label = 'MSE: {:.2f}, SSIM: {:.2f}, \n PSNR: {:.2f}, EN: {:.2f}'

# 为每一个subplot现实图像，设置标题
ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(label.format(mse_none, ssim_none, psnr_none, entropy_none))
ax[0].set_title('Original image')

ax[1].imshow(img_noise, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(label.format(mse_noise, ssim_noise, psnr_noise, entropy_noise))
ax[1].set_title('Image with noise')

ax[2].imshow(img_const, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[2].set_xlabel(label.format(mse_const, ssim_const, psnr_const, entropy_const))
ax[2].set_title('Image plus constant')

# 显示最后结果
plt.tight_layout()
plt.show()