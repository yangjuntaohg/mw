import requests
import time

url = "https://testv2.holla.world/api/Activities/MatchLottery/do"  # 中奖地址获取url


def main():
    """运行主方法，主要用于判断中奖概率。"""
    zhongjiang_count = 0  # 中奖的总数量
    data = {
        # 房间id
        "room_id": "5713455_624d539f816a5450316163",
        "token": "86210bee84380244960e053a02e0786d"
    }

    zhongjiang_dict = {}  # 总计中奖结果
    for i in range(1000):  # 循环1000次请求
        print("请求次数，目前是第 {} 次！".format(i))
        res = requests.post(url=url, data=data)
        if res.status_code == 200:
            res_json = res.json()
            res_data = res_json.get("data")
            prize = res_data.get("prize")
            if prize:  # 中奖信息json结构
                zhongjiang_count += 1  # 总计中奖次数加1
                zhongjaing_id = prize.get("id")  # 中奖的编码id
                if zhongjaing_id in zhongjiang_dict:  # 对中奖的编码id,如果是第一次抽中直接加入字典，并将默认值设置为1次，如果是非第一次抽中。字典对应的valuse增加1
                    zhongjiang_dict[zhongjaing_id] = zhongjiang_dict.get(zhongjaing_id) + 1
                else:
                    zhongjiang_dict[zhongjaing_id] = 1
                zhongjiang_count += 1  # 总计中奖次数加1
        else:
            print(res.status_code, res.text)  # 打印非200状态的数据返回结果，以及返回内容。
        time.sleep(0.5)  # 每次请求睡眠0.5秒，以减少后端服务器压力
    return zhongjiang_dict, zhongjiang_count


if __name__ == '__main__':
    zhongjiangjieguo, zhongjiang_count = main()
    print("中奖的总概率", zhongjiang_count / 1000)
    print("中奖的结果", zhongjiangjieguo)
    for k, v in zhongjiangjieguo.items():  # 输出每个中奖编号对应的中奖概率，的百分比
        print("奖品ID  {}  中奖概率是  {}".format(k, v / 1000))