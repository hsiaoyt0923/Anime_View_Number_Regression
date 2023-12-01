import requests
from bs4 import BeautifulSoup
import psycopg2
import password as pw
import random
import time
from fake_useragent import UserAgent


def download_tags(url: str) -> list[list]:
    # 建立隨機user_agent
    user_agent = UserAgent()

    # 開始爬蟲
    response = requests.get(url, headers={
                            "User-Agent": user_agent.random, "Referer": 'https://www.google.com.tw/', })
    response.encoding = 'utf8'
    if response.status_code == 200:
        print(f'請求成功：{response.status_code}')
    else:
        print(f'請求失敗：{response.status_code}')

    soup = BeautifulSoup(response.text, 'html.parser')
    anime_contents = soup.select('.anime_content')
    anime_tags = []

    for anime_content in anime_contents:
        anime_name = anime_content.select_one('.entity_localized_name').text
        tag_list = [anime_name]
        tags = anime_content.select('.anime_tag > tags')
        for tag in tags:
            tag_list.append(tag.text)
        tag_list = [tag_list[i] for i in range(3)]
        anime_tags.append(tag_list)
    print(anime_tags)
    return anime_tags


def insert_tags(conn, values: list[str]):
    values[0] = values[0].replace("'", "")
    values[0] = values[0].replace("2", "二")
    sql = f'''
        update 巴哈姆特動畫瘋
        set 原作載體='{values[1]}', 新續作='{values[2]}'
        where 動畫名='{values[0]}'
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()


def main():
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port=pw.PORT)
    print('資料庫連線成功')

    for i in ['2020', '2021', '2022', '2023']:
        for j in ['01', '04', '07', '10']:
            url = f'https://acgsecrets.hk/bangumi/{i+j}/'
            anime_tags = download_tags(url)
            for anime_tag in anime_tags:
                insert_tags(conn, anime_tag)

    conn.close()


if __name__ == '__main__':
    main()
