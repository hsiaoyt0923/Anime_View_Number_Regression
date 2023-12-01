import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
import password as pw
import time



def download_data(url: str) -> list[list]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'
    if r.status_code == 200:
        print(f'請求成功：{r.status_code}')
    else:
        print(f'請求失敗：{r.status_code}')
    intro_data = BeautifulSoup(r.text, 'html.parser')
    anime_infos = intro_data.select('.theme-list-main')
    anime_data = []
    for anime_info in anime_infos:
        show_view_number = anime_info.select_one(
            '.show-view-number > p').text.strip()
        anime_name = anime_info.select_one('.theme-name').text.strip()
        anime_time = anime_info.select_one(
            '.theme-time').text.strip().replace('年份：', '')
        anime_episode = anime_info.select_one(
            '.theme-number').text.strip().replace('共', '').replace('集', '')
        anime_link = 'https://ani.gamer.com.tw/' + anime_info['href']
        time.sleep(0.2)
        r1 = requests.get(anime_link, headers=headers)
        r1.encoding = 'utf8'
        detail_data = BeautifulSoup(r1.text, 'html.parser')
        acg_score = detail_data.select_one('.acg-score')
        star = acg_score.select_one('.score-overall-number').text.strip()
        rating_people = acg_score.select_one(
            '.score-overall-people').text.strip().replace('人評價', '').replace(',', '')
        type_list = detail_data.select_one('.type-list')
        staff = []
        tags = []
        pre_data = []
        for p in type_list.find_all('p'):
            staff.append(p.text)
        for li in type_list.select('.tag'):
            tags.append(li.text)
        infos = [anime_name, show_view_number, anime_time, anime_episode,
                 anime_link, star, rating_people, staff[1], staff[2], staff[3]]
        pre_data.append(infos)
        pre_data.append(tags)
        anime_data.append(pre_data)
        # print(f'動畫名:{anime_name}\n觀看數:{show_view_number}\n季度:{anime_time}\n集數:{anime_episode}\n動畫連結:{anime_link}\n{star}\n{rating_people}\n導演:{staff[1]}\n代理商:{staff[2]}\n製作廠商:{staff[3]}\n分類:{tags}\n')
    return anime_data


def create_table(conn) -> None:
    cursor = conn.cursor()
    cursor.execute(
        '''
    CREATE TABLE  IF NOT EXISTS 巴哈姆特動畫瘋(
	id SERIAL,
	動畫名 TEXT NOT NULL,
	觀看數 TEXT NOT NULL,
	季度 TEXT NOT NULL,
	集數 TEXT NOT NULL,
	動畫連結 TEXT NOT NULL,
	星級 TEXT,
	評分人數 TEXT,
	導演監督 TEXT NOT NULL,
	台灣代理 TEXT NOT NULL,
	製作廠商 TEXT NOT NULL,
	作品分類1 TEXT DEFAULT NULL,
	作品分類2 TEXT DEFAULT NULL,
	作品分類3 TEXT DEFAULT NULL,
	作品分類4 TEXT DEFAULT NULL,
	作品分類5 TEXT DEFAULT NULL,
	作品分類6 TEXT DEFAULT NULL,
	PRIMARY KEY(id),
	UNIQUE(動畫名)
    )
        '''
    )
    cursor.close()
    conn.commit()


def insert_data(conn, infos: list[str], tags: list[str]) -> None:
    # 避免作品標籤超過6個
    if len(tags) >= 7:
        tags = [tags[i] for i in range(6)]

    # column_names的必備元素
    column_names = [
        "動畫名", "觀看數", "季度", "集數", "動畫連結",
        "星級", "評分人數", "導演監督", "台灣代理", "製作廠商"
    ]

    # 依作品標籤數量增加column_names
    column_names += [f"作品分類{i + 1}" for i in range(len(tags))]

    # 基礎insert_sql
    insert_sql = f'''
        INSERT INTO 巴哈姆特動畫瘋
        ({','.join(column_names)})
        VALUES({','.join(['%s'] * len(column_names))})
        ON CONFLICT (動畫名) DO UPDATE SET
    '''
    # 基礎insert_sql + 更新內容
    update_columns = [f"{column_names[i]}='{infos[i]}'" for i in range(1, 7)]
    on_conflict_sql = ', '.join(update_columns)
    insert_sql += on_conflict_sql

    cursor = conn.cursor()
    cursor.execute(insert_sql, infos + tags)
    cursor.close()
    conn.commit()


def fetch_data(sql: str) -> list[tuple]:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port=pw.PORT)

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows


def last_page() -> int:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    response = requests.get(
        'https://ani.gamer.com.tw/animeList.php?', headers=headers)
    response.encoding = 'utf8'
    if response.status_code == 200:
        print(f'取得頁碼_訊息代號：{response.status_code}')
    else:
        print(f'取得頁碼_訊息代號：{response.status_code}')

    index = BeautifulSoup(response.text, 'html.parser')
    page_number = index.select_one('.page_number > a:last-child').text
    page_number = int(page_number)
    return page_number


def main():
    # 與資料庫建立連接
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port=pw.PORT)
    # 創建資料表
    create_table(conn)

    # 取得動畫列表最後一頁的頁碼
    page_number = last_page()

    # 開始逐頁下載資料
    n = 0
    for i in range(page_number):
        url = f'https://ani.gamer.com.tw/animeList.php?page={i+1}'
        anime_data = download_data(url)
        for infos_tags in anime_data:
            insert_data(conn, infos=infos_tags[0], tags=infos_tags[1])
        n += 1
        print(f'第{n}頁下載完畢')

    # 關閉資料庫
    conn.close()


if __name__ == '__main__':
    main()
