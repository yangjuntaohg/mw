import  requests
import json

def send():
    headers={'Cookie':'XSRF-TOKEN=eyJpdiI6IkZRRytNc3BzS1NodEx4WVpVOElCTmc9PSIsInZhbHVlIjoiRU9cLzRJaCsrTWNmd3Z6SWtGNldSaTdpTHBqRVZjSVhwUlQ3d2I2WlVTMWRPcjkrdlVzSlVoZDFpaE0yVWtmRTEiLCJtYWMiOiJmOTMzOWMxN2QyYTFjYWJhNWM5Zjg3ZjI2OTFlNjRhMzZmZWY2NDFmODM0YjJiYTZmZjkxYWE1YjdkMjY3MmJiIn0%3D; laravel_session=eyJpdiI6ImdKaWtoSXMwbFlqbVc3NTZDempDRmc9PSIsInZhbHVlIjoiUTZZYlZjOVNTSmZzSGlzRWtFcHpJcUI2dW53NXJOd3NkS0g2NWZOUFBYelhMTUZFK2tuZjFJelFqSDZyMWhJZCIsIm1hYyI6ImM5MmEyMjkxMTY2MTY1YTBmNGM4MGY2YTI5MDI1NTUxZDAzMTJmYjY2OTYwOGNjM2I4YmMzOTQyYjQ5ZTE1OWEifQ%3D%3D'
             ,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    url='http://admin2-sandbox.holla.world/admin/User/addGem'
    data='user_id=5719266&gems=200&gem_type=3'
    res=requests.post(url,data,headers=headers)
    print(res.text)


if __name__ == '__main__':
    for i in range(99):
        send()