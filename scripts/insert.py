# coding=utf-8
import pymysql
from nickname.scripts.config import con_test
from nickname.scripts.robottest import robot_test
import time

conn = pymysql.connect(host=con_test['host'], port=con_test['port'],
                       user=con_test['user'], password=con_test['password'],
                       database=con_test['database'])
cursor = conn.cursor(pymysql.cursors.DictCursor)

#查询
sql = "select id from acnt where login_channel = 7 limit 30"
cursor.execute(sql)
rs = cursor.fetchall()

#生成列表
idlist = [rs[i]['id'] for i in range(30)]

#插入
for i in idlist:
    insql = "INSERT INTO chacha.pc_girl_visit_history_records(user_id,target_user_id,created_at,updated_at) VALUES (5719411, {}, '2022-05-20 08:15:10', '2022-05-20 08:15:10');".format(i)
    cursor.execute(insql)
    conn.commit()
    time.sleep(0.1)

cursor.close()
conn.close()