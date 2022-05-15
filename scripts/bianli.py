import requests
import json

js={
"result": 0,
"message": "success",
"data": {
"reason_list": [{
"text": "Sexual Behavior",
"reason": "sex"
}, {
"text": "Incorrect Age",
"reason": "age"
}, {
"text": "Incorrect Gender",
"reason": "gender"
}, {
"text": "Rude/Bullying",
"reason": "rude"
}, {
"text": "Spam or Fraud",
"reason": "spam"
}, {
"text": "Others",
"reason": "others"
}],
"uid": 5719266,
"lang": "en"
}}

url='https://testv2.holla.world/api/User/Profile/report'



for i in range(1,7):
    # print(i)
    print(js['data']['reason_list'][i-1]['reason'])
    key = js['data']['reason_list'][i-1]['reason']
    data ={
    "token": "3ba1fdef50a4ab215ef8a3d7e00e3a46",
    "desc": "",
    "target_uid": "5718687",
    "reason": key,
    "images": []
    }
    res = requests.post(url=url,data=data)
    print(res.text)







