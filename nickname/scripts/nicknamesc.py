# coding=utf-8
import pymysql
from nickname.scripts.config import con
from nickname.scripts.robottest import robot_test
import time

# 连接
conn = pymysql.connect(host=con['host'], port=con['port'],
                       user=con['user'], password=con['password'],
                       database=con['database'])
cursor = conn.cursor(pymysql.cursors.DictCursor)

uids=(40564844,43560899,51712035,64435157,75263096)
usr=[]

# 执行
for i in uids:
    sql = "select first_name from acnt where id = {}".format(i)
    # print(sql)
    cursor.execute(sql)
    rs = cursor.fetchone()
    # print(rs)
    # [{'uid':1}]
    if rs['first_name'] == '':
        usr.append(i)

# 关闭
cursor.close()
conn.close()

# 打印
if usr == []:
    print('没有用户昵称为空'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
else:
    robot_test(usr)
    print('用户{}的昵称为空'.format(usr))
