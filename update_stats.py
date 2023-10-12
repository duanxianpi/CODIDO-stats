from bs4 import BeautifulSoup
import requests as re
import time
import os

currentYearMonth = time.strftime("%Y-%m")

now = time.time()

html = re.get('https://www.codido.co/marketplace/get_algo_cards').text

soup = BeautifulSoup(html, 'html.parser')

all_alogrithms = soup.select('div.row.row-cols-1.row-cols-md-2.row-cols-lg-4.g-4.card-group > div')

isStatsExist = os.path.exists(f"stats/stats-{currentYearMonth}.csv")

with open(f'stats/stats-{currentYearMonth}.csv', 'a') as f:
    if not isStatsExist:
        f.write("Timestamp,Name,Author,Ups,Runs\n")
    for alogrithm in all_alogrithms:
        name = alogrithm.select_one('div > div.card-body > h5').text.strip()
        author = alogrithm.select_one('div > div.card-footer > p').text.strip()[13:]
        ups = alogrithm.select_one('div > div.card-body > div > div:nth-child(1) > a').text.strip()
        runs = alogrithm.select_one('div > div.card-body > div > div:nth-child(2) > a').text.strip()
        
        f.write(f'{now},"{name}","{author}",{ups},{runs}\n')

