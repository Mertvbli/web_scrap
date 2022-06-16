import requests
import bs4
from pprint import pprint

url = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'Accept': 'application/json, text/plain, */*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cache-Control': 'no-cache',
           'Connection': 'keep-alive',
           'Cookie': '_ym_uid=1648822720578119853; _ym_d=1648822720; hl=ru; fl=ru; _ga=GA1.2.1137656088.1648822721; habr_web_home_feed=/all/; visited_articles=110731:349860:543760; _ym_isad=1; _gid=GA1.2.1429471187.1654754832',
           'Host': 'habr.com',
           'Pragma': 'no-cache',
           'Referer': 'https://habr.com/ru/all/',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
           'x-app-version': '2.77.0'
           }

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text
# print(text)
soup = bs4.BeautifulSoup(text, features='html.parser')
#print(soup)
articles = soup.find_all('article')
# print(articles)


for article in articles:
    text_title = article.find(class_='tm-article-snippet')
    # print(text_title.text)
    for key in KEYWORDS:
        if key in text_title.text or key.title() in text_title.text:
            time = article.find(class_='tm-article-snippet__datetime-published')
            time1 = time.find('time').text
            # print(time1)
            href1 = "https://habr.com" + article.find(class_='tm-article-snippet__title-link').get('href')
            title = article.find('h2').find('span').text
            #print(href1)
            result = f"{key}\n\t{time1} | {title} - {href1}"
            print(result)


