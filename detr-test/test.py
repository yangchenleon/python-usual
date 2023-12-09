from PIL import Image, ImageDraw, ImageFont
import requests
import torch
from transformers import AutoImageProcessor, DetrForObjectDetection

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

image_processor = AutoImageProcessor.from_pretrained("facebook/detr-resnet-50", proxies=proxies)
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", proxies=proxies)

inputs = image_processor(images=image, return_tensors="pt")
outputs = model(**inputs)

target_sizes = torch.tensor([image.size[::-1]])
results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[0]

# 创建高分辨率画布并将原图像映射到画布上
canvas_size = (image.width * 2, image.height * 2)
canvas = Image.new("RGB", canvas_size)
canvas.paste(image.resize(canvas_size), (0, 0))

draw = ImageDraw.Draw(canvas)

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [int(round(i * 2)) for i in box.tolist()]  # 将边界框坐标映射到高分辨率画布上
    label_text = f"{model.config.id2label[label.item()]} {round(score.item(), 3)}"
    draw.rectangle(box, outline="red", width=4)
    draw.text((box[0], box[1]), label_text, fill="red",font = ImageFont.truetype("arial.ttf", size=32))

# 保存图像
canvas.save("output.jpg")
print("图像保存成功！")