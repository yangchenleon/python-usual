import cv2
import torch
from torchvision.transforms import functional as F
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}
# 加载DETR模型和图像处理器
model_name = 'facebook/detr-resnet-50'
processor = DetrImageProcessor.from_pretrained(model_name, proxies=proxies)
model = DetrForObjectDetection.from_pretrained(model_name, proxies=proxies)

# 设置Webcam捕获
cap = cv2.VideoCapture(0)

# 降低分辨率的比例
scale_percent = 50

# 控制帧率的变量
frame_skip = 0
frame_skip_interval = 24  # 每5帧处理一次

while True:
    # 读取视频帧
    ret, frame = cap.read()

    # 控制帧率
    frame_skip += 1
    if frame_skip % frame_skip_interval != 0:
        continue
    
    # 调整分辨率
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    frame = cv2.resize(frame, (width, height))
    
    # 将图像转换为PIL图像
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # 使用图像处理器处理图像
    inputs = processor(images=pil_image, return_tensors="pt")
    
    # 使用DETR模型进行目标检测
    outputs = model(**inputs)
    results = processor.post_process_object_detection(outputs)[0]
    
    # 绘制检测框和标签
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        x, y, w, h = box
        x = int(x * width)
        y = int(y * height)
        w = int(w * width)
        h = int(h * height)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{model.config.id2label[label.item()]} {round(score.item(), 3)}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 显示帧
    cv2.imshow('Webcam', frame)
    
    # 按下'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()