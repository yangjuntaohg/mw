# coding=utf-8
from huafang.service.nickname.nickname import nickname
from time import sleep


def run():

    while True:
        uids=(5718391,5718399,5718621)
        nickname(uids)
        sleep(10)


if __name__ == '__main__':
    run()