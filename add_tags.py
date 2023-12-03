import requests
from bs4 import BeautifulSoup
import psycopg2
import password as pw
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
        per_anime = []
        anime_name = anime_content.select_one('.entity_localized_name').text
        other_names = anime_content.select_one('.anime_summary > i')
        if other_names is None:
            other_names = ''
        else:
            other_names = other_names.text.replace('其他名稱：', '')
        name_list = [anime_name] + other_names.split('、')
        tags = anime_content.select('.anime_tag > tags')
        tag_list = []
        for tag in tags:
            tag_list.append(tag.text)
        tag_list = [tag_list[i] for i in range(2)]
        per_anime.append(name_list)
        per_anime.append(tag_list)
        anime_tags.append(per_anime)
    return anime_tags


def insert_tags(conn, tags: list[list]):
    # 分離動畫名與標籤
    name_list = tags[0]
    tag_list = tags[1]

    # 去除動畫名中的"'"
    name_list = [name_list[i].replace("'", '') for i in range(len(name_list))]

    # 從最常用的動畫名翻譯中切出不同字串作模糊搜尋
    f_list = name_list[0].split()
    firstname = f_list[0]
    secondname = f_list[0][:4]
    thirdname = f_list[0][1:5]
    forthname = firstname.replace('~', '').replace('-', '').replace('‘', '')

    # 為了放入SQL語法中作處理
    namestr = ''
    for item in name_list:
        namestr += f"'{item}'"
        namestr += ','
    namestr = namestr.rstrip(',')

    print(namestr)
    print(firstname)
    print(secondname)

    sql = f'''
        update 動畫瘋訓練資料集
        set 原作載體='{tag_list[0]}', 新續作='{tag_list[1]}'
        where 動畫名 in ({namestr})
        or 動畫名 like '%{firstname}%'
        or 動畫名 like '%{secondname}%'
        or 動畫名 like '%{thirdname}%'
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


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
            print(f'{i+j}新番下載成功')
            for anime_tag in anime_tags:
                insert_tags(conn, tags=anime_tag)
                conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
