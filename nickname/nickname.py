# coding=utf-8
import pymysql
from nickname.config.config import con
from nickname.common.robot import sendmsg


def nickname(uids):

    # 连接
    conn = pymysql.connect(host=con['host'], port=con['port'],
    user=con['user'], password=con['password'],
    database=con['database'])
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    usr = []
    # 执行
    for i in uids:
        sql = "select first_name from acnt where id = {}".format(i)
        # print(sql)
        cursor.execute(sql)
        rs = cursor.fetchone()
        # print(rs)
        #[{'uid':1}]
        if rs['first_name']!='':
            usr.append(i)

    # 关闭
    cursor.close()
    conn.close()

    # 消息
    if usr == []:
        print('没有用户昵称为空')
        return None
    else:
        sendmsg(usr)
        print('用户{}的昵称为空'.format(usr))
        return usr


if __name__ == "__main__":
    uids=(5718391,5718399,5718621)
    nickname(uids)