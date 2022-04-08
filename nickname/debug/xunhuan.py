
def nickname(uids):

    usr = []
    # 执行
    for i in uids:
        rs=[{'uid':''}]
        if rs[0]['uid'] == '':
            usr.append(i)
    print(usr)


if __name__ == '__main__':
    uids = (1,2,3)
    nickname(uids)