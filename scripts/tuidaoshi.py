#1
rs = [{'id': 5719969}, {'id': 5719968}]
idlist=[rs[i]['id'] for i in range(30)]
print(idlist)

idls=[]
for i in range(30):
    idls.append(rs[i]['id'])
print(idls)


#2
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

list = [js['data']['reason_list'][i-1]['reason'] for i in range(1,7)]
print(list)