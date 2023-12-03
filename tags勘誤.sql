alter table 動畫瘋訓練資料集
drop column 原作載體,
drop column 新續作

alter table 動畫瘋訓練資料集
add column 原作載體 text,
add column 新續作 text

select * from 動畫瘋訓練資料集 order by id

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 order by id

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 原作載體 is null or 新續作 is null order by 動畫名

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%賢者時間%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%鬼滅%'

select id, 動畫名, 年份, 月份, 原作載體, 新續作 from 動畫瘋訓練資料集 where 動畫名 like '%星光王子%'

update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%星光王子%'

update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='續作' where 動畫名 like '%男子游泳部%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%GIVEN%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%從零開始的異世界生活%'

update 動畫瘋訓練資料集 set 原作載體='小說改編', 新續作='新作' where 動畫名 like '%僕愛君愛%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%鬼滅%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名 like '%賢者時間%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%賢者時間%' and 動畫名 like '%Extra%'

update 動畫瘋訓練資料集 set 新續作='新作' where 動畫名 like '%第一季%'

update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%超人力霸王%'

update 動畫瘋訓練資料集 set 原作載體='原創作品', 新續作='續作' where 動畫名 like '%假面騎士%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%網球王子%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%忍者哈特利%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='續作' where 動畫名 like '%麵包超人%'

update 動畫瘋訓練資料集 set 原作載體='漫畫改編', 新續作='新作' where 動畫名 like '%叫我對大哥%'

update 動畫瘋訓練資料集 set 新續作='續作' where 動畫名 like '%第二季%'