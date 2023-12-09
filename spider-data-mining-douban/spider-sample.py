import requests
import re

def PaChong(url):
    f = open("top2500.csv", mode="a", encoding="utf-8")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span'
                     r'>.*?<p class="">.*?导演:(?P<daoyan>.*?) .*?...<br>'
                     r'(?P<year>.*?) .*?property="v:average">(?P<rate>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',
                     re.S)
    result = obj.finditer(response.text)
    for item in result:
        name = item.group("name")
        daoyan = item.group("daoyan")
        year = item.group("year").strip()
        rate = item.group("rate")
        num = item.group("num")
        f.write(f"{name},{daoyan},{year},{rate},{num}\n")
        print(r"电影名：",name,"导演:",daoyan,"主演:  syy   年份：",year,"豆瓣评分:",rate,"观看人数:",num)

    f.close()
    response.close()
    print("豆瓣250提取完毕")

if __name__ == "__main__":
    turn=int(input("请输入要爬取得页数："))
    for i in range(1,turn+1):
        if i==1:
            url = "https://movie.douban.com/top250"
        else:
            url = "https://movie.douban.com/top250?start="+str((i-1)*25)+"&filter="
        print(url)
        PaChong(url)