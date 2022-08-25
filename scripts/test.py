import requests
import json
import xlrd

workbook = xlrd.open_workbook(filename=str('/Users/edy/Desktop/xls.xls'))
# 获取sheet
table = workbook.sheets()[0]
# table_row = table.row_values(rowx=0, start_colx=0, end_colx=None)
# print(table_row)
# 获取表格列生成list
table_col = table.col_values(colx=0, start_rowx=0, end_rowx=None)

# 异常字典
nottrue = {}
# print(lst,'\n')
for i in table_col:
    # print(i)
    url = 'http://api-sandbox.camproapp.com/api/Profile/FirstName/check'
    data = {'name': '', 'first_name': i}
    # print(data)
    res = json.loads(requests.post(url=url, data=data).text)
    # print(res,'\n')
    if 'status' in res['data'] and res['data']['status'] is True:
        continue
    else:
        nottrue[i] = res
# nottrue = json.dumps(nottrue)
print(nottrue)

headers = {'Content-Type': 'application/json'}
# url='https://open.feishu.cn/open-apis/bot/v2/hook/b6826623-951c-4efc-9b9b-e1278b142fe8'
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/cd5b49bd-d9cc-4a1f-9ddf-920b8ea13775'
dic = {'msg_type': 'text', 'content': {'text':'{}'.format(nottrue)}}
print(dic)
# print(str(dic))
data = json.dumps(dic)
# print(data)
rs = requests.post(headers=headers, data=data, url=url)
print(rs.text)
