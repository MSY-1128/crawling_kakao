import requests
from bs4 import BeautifulSoup as bs


kakao_career_url = 'https://careers.kakao.com/jobs'
search_board_tr = '#mArticle > div > ul.list_jobs > li > div'
search_title = 'div > a'
search_date = 'div > dl > dd:nth-of-type(1)'

req = requests.get(kakao_career_url)
html = req.text
# print(html)

soup = bs(html,'lxml')
board_list = soup.select(search_board_tr)
# print(board_list)
for index, kakao_board_list in enumerate(board_list):
    title_list = kakao_board_list.select_one(search_title)
    # print(title_list)
    kakao_board_title = title_list.text
    kakao_board_title = kakao_board_title.strip()
    # print(kakao_board_title)
    date_list = kakao_board_list.select_one(search_date)
    kakao_board_date = date_list.text # 원래는 날짜인데 해당 사이트는 영입종료시로 표현되어있음
    # print(kakao_board_date)