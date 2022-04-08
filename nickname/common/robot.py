# coding=utf-8
import requests
import json


def sendmsg(msg):

    headers={'Content-Type': 'application/json'}
    url='https://open.feishu.cn/open-apis/bot/v2/hook/ae157469-8666-49fe-9e27-7936de79b5e4'

    dic={"msg_type":"text","content":{"text":"用户{}的昵称为空，请关注".format(msg)}}
    # print(str(dic))
    data=json.dumps(dic)
    # print(data)
    rs=requests.post(headers=headers,data=data,url=url)
    # print(rs.text)


if __name__ == '__main__':
    sendmsg('test')
