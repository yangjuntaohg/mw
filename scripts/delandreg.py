import requests
import json
import easygui as g
import httplib2
i = 0
app_version = "4.4.6"
#获得输入参数
user_access_token = g.enterbox(msg='请输入user_access_token',title='皮皮鱼',default=None,strip=None)
#可以设置默认Facebook token，将默认token填到此代码处避免每次输入
if user_access_token == "ppy":
    user_access_token = "EAAYnNsVlAkUBACpszVqbrsGphxEmTJrs0lY78vEtY7jD1TpRYiq8xIZCPvZBzHPaMKPqkCuyMHLcdkImgPpVxLdKCg4tNOPzRYUhVwYPLYBrQPrX9OinUSk92HdZB0ZAXqCyBYEObWSvfyfXV5jwzI9AnT899zHXh6RZCOIsDVB4FZAGktYperEK1601mOdfLPVPe1Nhm9WLmeUZBRjsffSQbqyZAxxsoENQ8ZAVjrhUu5gZDZD"
choice = g.buttonbox(msg = '需要指定尾数or循环次数？', choices = ('指定尾数', '循环次数','删除账号'))
if choice == "指定尾数":
    id_tail_need = g.integerbox(msg='请输入需要的尾数', title='皮皮鱼', default=None,lowerbound=0, upperbound=99, image=None, root=None)
elif choice == "循环次数":
    cycle_need = g.integerbox(msg='请输入需要的尾数', title='皮皮鱼', default=None, lowerbound=0, upperbound=99, image=None,root=None)
    cycle = 0
#获取cookie
url = "http://hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com/admin/auth/login"
payload = "username=yu.li%40holla.world&password=asdfghjkl&_token=EIRqhKnaUJlIXwC8ArF1ujEHtVmNevKEgTo0wnR5"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d3970b37-e109-41f6-a4b4-351dfbd0f721,cfdd4492-48ce-4875-bf2f-2306ce5142e1",
    'accept-encoding': "gzip, deflate",
    'referer': "http://hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com/admin/auth/login",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
response = requests.request("POST", url, data=payload, headers=headers)
cookies = requests.utils.dict_from_cookiejar(response.cookies)
cookie = "XSRF-TOKEN=" + cookies.get("XSRF-TOKEN") + ";" + "laravel_session=" + cookies.get("laravel_session")
#主函数
while True:
    i += 1
    #获取id
    payload = {
    "app_version": app_version,
    "device_id": "87E7BE554C755503F324A341ACA4B389",
    "user_access_token": user_access_token,
    "language": "en",
    "phone_model_name": "iPhone 5s",
    "timezone": 8
    }
    url = "http://testv2.holla.world/api/Account/loginWithFacebook"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    temp = json.loads(r.text)
    id_old = temp.get("data").get("user").get("id")
    #删掉账号
    url = "http://hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com/admin/User/removeUser"
    payload = "id=%s&_method=post&_token=OZgaMInjzrY4q1U97QiQmD3ezvLoQ6L3dekEMlFu"%id_old
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'Origin': "http://hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com",
    'Referer': "http://hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com/admin/users",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "bd0c3571-cdb8-47fb-9272-df83a6b108b3,ad0b4ffa-0024-4d7b-b710-df09796b7dbb",
    'Host': "hollaadmin-env.pnwxvfg2mr.ap-northeast-1.elasticbeanstalk.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "71",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
    'cookie':cookie
    }
    response = requests.request("POST", url, data=payload, headers=headers, allow_redirects = False)
    status_code = response.status_code
    if status_code!=200:
        print("Cookie ERROR!")
        break
    #重新使用Facebook注册登录
    payload = {
    "app_version": app_version,
    "device_id": "87E7BE554C755503F324A341ACA4B389",
    "user_access_token": user_access_token,
    "language": "en",
    "phone_model_name": "iPhone 5s",
    "timezone": 8
    }
    url = "http://testv2.holla.world/api/Account/loginWithFacebook"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    temp = json.loads(r.text)
    id_new = temp.get("data").get("user").get("id")
    id_tail=int(str(id_new)[-1])
    print("旧id",id_old,"删除又注册成功为新id",id_new)
    if choice == "指定尾数":
        if id_tail == id_tail_need :
            break
    elif choice == "循环次数":
        cycle += 1
        if cycle == cycle_need:
            break
    else:
        break