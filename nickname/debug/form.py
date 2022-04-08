

def form(uids):

    sql = "select nickname from user_tokens where user_id = {}".format(uids)
    print(type(sql),sql)


if __name__ == '__main__':
    uids=(1)
    form(uids)
    list=[1,2,3]
    print('str {}'.format(list))