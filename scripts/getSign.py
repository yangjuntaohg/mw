import base64
import time
import json
import hmac

def now_time():
    t = time.time()
    # print (t) # 原始时间数据
    # print (int(t)) # 秒级时间戳
    # print (int(round(t * 1000))) # 毫秒级时间戳
    nowTime = lambda: int(round(t * 1000))
    # print (nowTime)
    print(nowTime())
    return nowTime()

def hmac_sha256_encrypt(key, data):
    key = key.encode('utf-8')  # sha256加密的key
    message = data.encode('utf-8')  # 待sha256加密的内容
    sign = base64.b64encode(hmac.new(key, message, digestmod='sha256').digest()).decode()
    return sign

def strSign(body, uri, method, appid, deviceid):
    signStr = json.dumps(body) + str(uri) + str(method.upper()) + str(appid) + str(deviceid) + str(now_time()).replace(" ","")
    secret = 'qhQcDjxycwSl1vTu7k1wXIr3I1TWGGNz'
    hmac_sha256_encrypt(secret, signStr)

def sendSMSCode():
    uri = '/api/v1/verifycode/request'
    data = {
        "country_prefix": "1",
        "national_number": "6096140742",
        "number": "16096140742"
    }
    header_sendSMSCode = {
        "signature": strSign(data, uri, method, appid, deviceid),
        "app-id": appid,
        "device": "android",
        "device-id": deviceid,
        "version": "4.7.0",
        "app-lang": "en",
        "Content-Type": "application/json",
        "timestamp": str(nowTime)
    }
    response = doRequest("post", url=host + uri, header=header_sendSMSCode, data=data)
    print(response['data'])
    return response['data']


def getSMSCode():
    uri = '/internal/v1/verifycode?phone_number=16096140742'
    data = {}
    response = doRequest("get", url=host + uri, header=header_getSMSCode, data=data)
    print(response['data'])
    return response['data']

def get_user_access_token():
    uri = '/api/v1/verifycode/verify'
    data = {
        "phone": {
            "country_prefix": "1",
            "national_number": "6096140742",
            "number": "16096140742"
        },
        "code": getSMSCode()
    }
    header_access_token = {
        "signature": strSign(data, uri, method, appid, deviceid),
        "app-id": appid,
        "device": "android",
        "device-id": deviceid,
        "version": "4.4.0",
        "Content-Type": "application/json",
        "timestamp": str(nowTime),
        "app-lang": "en",
        "Host": "apitest.omegle.fun"
    }
    response = doRequest("post", url=host + uri, header=header_access_token, data=data)
    print(response['data'])
    return response['data']

def loginWithAccountKit():
    sendSMSCode()
    uri = '/api/Account/loginWithAccountKit'
    data = {
        "user_access_token": get_user_access_token(),
        "app_version": "4.7.0",
        "bddid": "JRLANH2UKA4XCT2GVPLKCDJALIYWC6TJ5TDQ36L7RCUQXJ6GDM7Q01",
        "bundle_id": "ly.omegle.android",
        "device_id": deviceid,
        "language": "en",
        "phone_model_name": "Xiaomi Redmi 4X",
        "shumei_device_id": "20220721143439d8181df2799250cea71f2c834f950b8d0155795fd1764cbf",
        "timezone": 8,
        "access_token_type": "monkey_account_kit"
    }
    response = doRequest("post", url=host_omgea + uri, header=header, data=data)
    print(response['data']['user']['token'])
    return response['data']['user']['token']

if __name__ == '__main__':
    now_time()