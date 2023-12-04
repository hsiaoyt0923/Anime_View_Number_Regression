alter table 動畫瘋訓練資料集
drop column 原作載體,
drop column 新續作

alter table 動畫瘋訓練資料集
add column 原作載體 text,
add column 新續作 text


--搜尋指令
select * from 動畫瘋訓練資料集 order by id

select * from 巴哈姆特動畫瘋 where 動畫名 like '%LOAD%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 order by id

select id, 動畫名, 總觀看數, 平均觀看數, 集數, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 年份='2023'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 原作載體 is null or 新續作 is null order by 動畫名

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%賢者時間%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%鬼滅%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%星光王子%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%水星領航員%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%小鳥之翼%'


--將月份轉為春、夏、秋、冬
select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 月份 not in ('冬番','春番','夏番','秋番')
update 動畫瘋訓練資料集 set 月份='冬番' where 月份 in ('01','02','03')
update 動畫瘋訓練資料集 set 月份='春番' where 月份 in ('04','05','06')
update 動畫瘋訓練資料集 set 月份='夏番' where 月份 in ('07','08','09')
update 動畫瘋訓練資料集 set 月份='秋番' where 月份 in ('10','11','12')


--針對程式無法自動填入的標籤進行手動更正
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%鬼滅%'
update 動畫瘋訓練資料集 set 新續作='新作' where 動畫名='鬼滅之奏'
update 動畫瘋訓練資料集 set 新續作='新作' where 動畫名='國高中一貫！！鬼滅學園物語'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編' where 動畫名 like '%水星領航員%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%GIVEN%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名 like '%賢者時間%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%賢者時間%' and 動畫名 like '%Extra%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%網球王子%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%忍者哈特利%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%麵包超人%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名 like '%叫我對大哥%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%ACCA%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='BURN THE WITCH 龍與魔女'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='遊戲王! SEVENS'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='汪汪與喵喵'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='房間露營'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='東方少年'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='東京 24 區'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%世界一初戀～求婚編～%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名 like '%無神世界的神明活動%'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='川尻小玉的懶散生活'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='藍色監獄'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='魔法水果籃 -前奏曲-'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='我們的黎明'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='急戰 5 秒殊死鬥'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='幼女社長'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='加油吧同期醬'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名='酷愛電影的龐波小姐'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名='最遊記 RELOAD -ZEROIN-'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名='烙印勇士 黃金時代篇 MEMORIAL EDITION 年齡限制版'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名='銀河騎士傳 織愛之星'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名='天使降臨到我身邊！珍貴的朋友'
update 動畫瘋訓練資料集 set 原作載體='漫畫改編' where 動畫名 like '星期一的豐滿%'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='續作' where 動畫名 like '%男子游泳部%'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='續作' where 動畫名 like '%從零開始的異世界生活%'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='新作' where 動畫名 like '%僕愛君愛%'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='新作' where 動畫名='勇者、辭職不幹了'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='續作' where 動畫名='艾梅洛閣下 II 世事件簿 -魔眼蒐集列車 Grace note- 特別篇'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='新作' where 動畫名='海岬的迷途之家'
update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='新作' where 動畫名='鹿王'
update 動畫瘋訓練資料集 set 原作載體='小說改編' where 動畫名 like '%打工吧，魔王大人！%'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='新作' where 動畫名='ICHU 偶像進行曲'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='新作' where 動畫名 like '%MUV-LUV ALTERNATIVE%'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='新作' where 動畫名='白貓 Project Zero Chronicle 零之紀元'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='續作' where 動畫名='暮蟬悲鳴時 業'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='續作' where 動畫名='艦隊 Collection 總有一天，在那片海'
update 動畫瘋訓練資料集 set 原作載體='遊戲改編', 新續作='續作' where 動畫名 like '%薄櫻鬼%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='奇米萌 CHIMIMO'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%歌之☆王子殿下%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名='魔神英雄傳 七魂的龍神丸 -再會-'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名='BUILD-DIVIDE -#FFFFFF- CODE WHITE'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='DECA - DENCE'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='Futsal Boys！！！！！'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%星光王子%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='白沙的 Aquatope'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%少女與戰車%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%天地無用%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='讓我聽見愛的歌聲'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='血汗英雄全泰壹'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名 like '%絆之 Allele%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='境界服務'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='扶桑花女孩之舞'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='水豚君'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='噴嚏大魔王 2020'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名='荒野的壽飛行隊 完全版'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='座敷童子塌塌米醬'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名='淘氣貓 2020：家有圓圓？！我家的圓圓你知道嗎～'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名 like '%MEGALOBOX%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名 like '%視覺監獄%'
update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='新作' where 動畫名 like '%WAVE!! ~來衝浪吧!!~%'
update 動畫瘋訓練資料集 set 原作載體='原創作品' where 動畫名 like '%小鳥之翼%'
update 動畫瘋訓練資料集 set 新續作='續作' where 動畫名 like '%第二季%'
update 動畫瘋訓練資料集 set 新續作='新作' where 動畫名 like '%第一季%'


--刪除電影、舞台劇、特攝英雄、兒童向動畫
delete from 動畫瘋訓練資料集 where 動畫名='TEN·豪快者'
delete from 動畫瘋訓練資料集 where 動畫名='機界戰隊全開者 VS 煌輝者 VS 前輩者'
delete from 動畫瘋訓練資料集 where 動畫名='魔進戰隊煌輝者 VS 龍裝者'
delete from 動畫瘋訓練資料集 where 動畫名='我的泰山爸爸'
delete from 動畫瘋訓練資料集 where 動畫名='暴走哈姆醬'
delete from 動畫瘋訓練資料集 where 動畫名='夏目友人帳特別上映版：喚石與可疑訪客'
delete from 動畫瘋訓練資料集 where 動畫名='偶像學園 Planet!'
delete from 動畫瘋訓練資料集 where 動畫名='鳴鳥不飛：烏雲密布'
delete from 動畫瘋訓練資料集 where 動畫名='有貓注意！'
delete from 動畫瘋訓練資料集 where 動畫名='小怪獸成長日記 第二季'
delete from 動畫瘋訓練資料集 where 動畫名='垃圾總動員'
delete from 動畫瘋訓練資料集 where 動畫名='寶可夢：皮卡丘與可可的冒險'
delete from 動畫瘋訓練資料集 where 動畫名='寶可夢：皮卡丘與可可的冒險'
delete from 動畫瘋訓練資料集 where 動畫名='築夢奇蹟'
delete from 動畫瘋訓練資料集 where 動畫名='銀龍出任務'
delete from 動畫瘋訓練資料集 where 動畫名='烘焙小精靈'
delete from 動畫瘋訓練資料集 where 動畫名='整容液'
delete from 動畫瘋訓練資料集 where 動畫名='喵的咧～貓咪戲說日本史！第五季'
delete from 動畫瘋訓練資料集 where 動畫名='怪物彈珠 THE MOVIE 路西法 絕望的黎明'
delete from 動畫瘋訓練資料集 where 動畫名='交錯的想念'
delete from 動畫瘋訓練資料集 where 動畫名='海邊的異邦人'
delete from 動畫瘋訓練資料集 where 動畫名='秘密結社 鷹之爪 -Golden Spell-'
delete from 動畫瘋訓練資料集 where 動畫名='阿松～希皮波族與閃耀果實～'
delete from 動畫瘋訓練資料集 where 動畫名 like '%假面騎士%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%超人力霸王%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%戰士美少女%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%衝鋒戰士%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%舞台劇%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%劇場版%'
delete from 動畫瘋訓練資料集 where 動畫名 like '%電影版%'
delete from 動畫瘋訓練資料集 where 集數=1
