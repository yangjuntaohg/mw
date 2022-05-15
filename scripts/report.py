import  requests
import json


def send():
    url='https://testv2.holla.world/api/User/Profile/reportReasonList'
    data={"token": "3ba1fdef50a4ab215ef8a3d7e00e3a46"}
    # print(data)
    # print(json.dumps(data))
    res=requests.post(url,data)
    print(res.text)


if __name__ == '__main__':
        send()