import requests
proxies={
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890'
}
response=requests.get('https://www.huggingface.co/facebook/detr-resnet-50/resolve/main/config.json',proxies=None)
print(response.text)