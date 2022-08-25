# coding=utf-8
import requests
import json


def robot_test(str1):

    headers={'Content-Type': 'application/json'}
    # url='https://open.feishu.cn/open-apis/bot/v2/hook/b6826623-951c-4efc-9b9b-e1278b142fe8'
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/cd5b49bd-d9cc-4a1f-9ddf-920b8ea13775'
    dic={"msg_type":"text","content":{"text":"用户{}的昵称为空，请关注".format(str1)}}
    print(str(dic))
    data=json.dumps(dic)
    print(data)
    # data='{"msg_type":"text","content":{"text":"request example"}}'

    rs=requests.post(headers=headers,data=data,url=url)
    print(rs.text)


if __name__ == '__main__':
    robot_test('test')
