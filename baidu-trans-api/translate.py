import requests, os
import hashlib

from utils.alpha.latextotext import tex2txt
from utils.alpha.texttolatex import txt2tex
from utils.beta.tex2txt import tex2txt2
from utils.beta.txt2tex import txt2tex2

# 百度翻译 API 请求地址
url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

# 设置你的 API Key
appid = '20201208000642175'
salt = '1435660288'
secret_key = 'vkHsqtmp64OjUr8P6BKJ'

# 使用百度翻译 API 进行翻译
def translate_text(text, from_lang, to_lang):
    str1 = appid + text + salt + secret_key
    params = {
        'q': text,
        'from': from_lang,
        'to': to_lang,
        'appid': appid,
        'salt': salt,
        'sign': hashlib.md5(str1.encode('utf-8')).hexdigest()
    }
    response = requests.get(url, params=params)
    result = response.json()
    translated_text = result['trans_result'][0]['dst']
    return translated_text


# 读取文本文件内容
def trans_file(input_path, output_path, from_lang, to_lang):
    
    input_file = open(input_path, 'r', encoding='utf-8')
    input = input_file.readlines()
    input_file.close()
    clean_file(output_path)
    for line in input:
        line = line.strip()
        if line == '':
            translated_text = ''
        else:
            translated_text = translate_text(line, from_lang, to_lang)
        with open(output_path, 'a', encoding='utf-8') as output:
            output.write(translated_text + '\n')
    # line = input.readline()

def clean_file(file_path):
    with open(file_path, "w") as file:
        file.write("")  # 将空字符串写入文件

if __name__ == '__main__':
    input_dir = 'D:\Workspace\paper-workspace\pfl-survey-paper-cn\contents'
    output_dir = 'D:\Workspace\paper-workspace\pfl-survey-paper-cn\contents-en'
    
    # tex2txt2('from.tex')
    # trans_file('aux.txt', 'aux1.txt', 'zh', 'en')
    # txt2tex2('result.tex')
    
    # 最好不要中英混搭，在zh-en环境下，一段内en过多，会导致剩下的中文不翻译
    # 注意如何翻译结果txt切换，相应txt2tex要变换输入文件
    # for file in os.listdir(input_dir):
    #     tex2txt2(os.path.join(input_dir, file))
    #     trans_file('aux.txt', 'aux1.txt', 'zh', 'en')
    #     txt2tex2(os.path.join(output_dir, file))
    # os.remove('aux.dic')
    os.remove('aux.txt')
    os.remove('gtexfix_commands')
    os.remove('gtexfix_comments')
    os.remove('gtexfix_latex')    
    