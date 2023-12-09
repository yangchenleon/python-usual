import pandas as pd
import requests
import time
import csv


def save_image(film_name, img_url):
    image = requests.get(img_url).content
    film_name.replace('/', '-')
    img_name = film_name + '.' + img_url.split('.')[-1]
    with open('./经典电影图片/%s' % img_name, 'wb')as file:
         file.write(image)

def deal_film_list(films_list):
    films, scores, arrts, counties, film_time = [], [], [], [], []
    films_data = []
    for film in films_list:
        rank = film['rank']
        name = film['title']
        score = float(film['rating'][0])
        release_date = int(film['release_date'][:4])
        types = film['types']
        regions = film['regions']
        
        types = ','.join(types) if len(types) > 1 else types[0]
        regions = ', '.join(regions) if len(regions) > 1 else regions[0]
        img_url = film['cover_url']
        # save_image(name, img_url)

        films.append(name)
        scores.append(score)
        arrts.append(types)
        counties.append(regions)
        film_time.append(release_date)
        films_data.append([name, score, release_date, types, regions])
    return films_data

def init_file():
    colums=['films', 'scores', 'film_time', 'arrts', 'counties']
    datafile=pd.DataFrame(None, columns=colums)
    datafile.to_csv('./film_info.csv', mode='w', encoding='utf-8', header=True, index=False)

def write_file(films_data):
    datafile=pd.DataFrame(films_data, columns=['films', 'scores', 'film_time', 'arrts', 'counties'])
    # datafile.index = [index for index in range(1,len(datafile.index)+1)]
    datafile.to_csv('./film_info.csv', mode='a', encoding='utf-8', header=False, index=False)

def gen_urls(num_films=2000, limit=50):
    # can't read last interval 10-0 and detect max film number.
    url_base = "https://movie.douban.com/j/chart/top_list?type=11&interval_id={}%3A{}&action=0&start={}&limit={}"
    urls = []
    cur_idx = 0
    for i in range(90, 0, -10):
        start = 0
        url = url_base.format(i, i - 10, 0, 1)
        page_cont = gen_json(url)
        
        max_idx = min(page_cont[0]['rank'] - 1, num_films)
        end = max_idx - cur_idx
        cur_idx = max_idx

        for j in range(start, end - limit, limit):
            urls.append(url_base.format(i + 10, i, j, limit))
        remain = end // limit * limit
        urls.append(url_base.format(i + 10, i, remain, end - remain))
    return urls
    
def gen_json(url):
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    reponse=requests.get(url,headers=header)
    time.sleep(5)
    aim=reponse.json()
    return aim

if __name__ == '__main__':
    init_file()
    for url in gen_urls():
        films_data = deal_film_list(gen_json(url))
        write_file(films_data)
