import requests
from scripts.getcollist import getcollist
import json


def checkname_single(first_name):
    url = 'http://api-sandbox.camproapp.com/api/Profile/FirstName/check'
    data = {'name': '', 'first_name': first_name}
    res=json.loads(requests.post(url=url,data=data).text)
    print(res)


def checkname_batch(path):
    #异常字典
    nottrue={}
    #调用getcollist获取测试列表
    lst = getcollist(path)
    # print(lst,'\n')
    for i in lst:
        # print(i)
        url = 'http://api-sandbox.camproapp.com/api/Profile/FirstName/check'
        data={'name':'','first_name':i}
        # print(data)
        res=json.loads(requests.post(url=url,data=data).text)
        # print(res,'\n')
        if 'status' in res['data'] and res['data']['status'] is False:
            continue
        else:
            nottrue[i]=res
    #打印异常结果
    print(nottrue)


if __name__ == '__main__':
    #待测Excel文件路径
    path = '/Users/edy/Desktop/xls.xls'
    checkname_batch(path)
    #单接口测试
    # checkname('🔞Elisa🍼')
    # checkname('yangsea')
    # checkname('fb juntao')