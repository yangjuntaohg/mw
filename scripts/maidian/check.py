def check_data(excel_data, redshift_data):
    print('开始解析！')
    err_data = []
    all_data = []
    for i in excel_data:
        event_data = []
        attributes_data = []
        user_properties_data = []
        type_data = []
        value_data = []
        for j in redshift_data:
            if "event" in i:
                print("event存在!")
                if i.get("event") == j[0]:
                    print(str(i.get("event")) + "找到相同event!")
                    event_data.append(i)
                    if "attributes" in i:
                        print("attributes存在！")
                        if i.get("attributes") in j[1]:
                            print(str(i.get("attributes")) + "找到相同attributes!")
                            attributes_data.append(i)
                            print(str(i.get("user_properties_data")) + "attributes存在user_properties_data必然为空不需要校验！")
                            user_properties_data.append(i)
                            if "type" in i:
                                print("type存在!")
                                if i.get("type") == "无":
                                    type_data.append(i)
                                    print("type为空不需要校验type!")
                                elif i.get("type") == str(type(json.loads(j[1]).get(i.get("attributes")))).split("'")[1]:
                                    type_data.append(i)
                                    print(str(i.get("type")) + "type相等")
                                    if "value" in i:
                                        print("value存在！")
                                        if i.get("value") == "无":
                                            value_data.append(i)
                                            print("value为空不需要校验value!")
                                            break
                                        elif i.get("value") == json.loads(j[1]).get(i.get("attributes")):
                                            value_data.append(i)
                                            print(str(i.get("value")) + "value相等")
                                            break
                                        else:
                                            print(str(i.get("value")) + "value不等!")
                                            err_data.append('此事件内的参数类型错误!事件信息:{}'.format(i.get("event")))
                                            continue
                                    else:
                                        print(str(i.get("type")) + "type不等!")
                                        err_data.append('此事件内的参数类型错误!事件信息:{}'.format(i.get("event")))
                            else:
                                print("type不存在!")
                        elif i.get("attributes") == "无":
                            attributes_data.append(i)
                            print("attributes为空不需要校验attributes!")
                            if "user_properties" in i:
                                print("user_properties存在！")
                                if i.get("user_properties") in j[2]:
                                    print(str(i.get("user_properties")) + "找到相同user_properties!")
                                    user_properties_data.append(i)
                                    if "type" in i:
                                        print("type存在!")
                                        if i.get("type") == "无":
                                            type_data.append(i)
                                            print("type为空不需要校验type!")
                                        elif i.get("type") == \
                                                str(type(json.loads(j[2]).get(i.get("user_properties")))).split("'")[1]:
                                            type_data.append(i)
                                            print(str(i.get("type")) + "type相等")
                                            if "value" in i:
                                                print("value存在！")
                                                if i.get("value") == "无":
                                                    value_data.append(i)
                                                    print("value为空不需要校验value!")
                                                    break
                                                elif i.get("value") == json.loads(j[2]).get(i.get("user_properties")):
                                                    value_data.append(i)
                                                    print(str(i.get("value")) + "value相等")
                                                    break
                                                else:
                                                    print(str(i.get("value")) + "value不等!")
                                                    err_data.append('此事件内的参数类型错误!事件信息:{}'.format(i.get("event")))
                                                    continue
                                        else:
                                            print(str(i.get("type")) + "type不等!")
                                            err_data.append('此事件内的参数类型错误!事件信息:{}'.format(i.get("event")))
                                    else:
                                        print("type不存在!")
                                elif i.get("user_properties") == "无":
                                    user_properties_data.append(i)
                                    type_data.append(i)
                                    value_data.append(i)
                                    print("attributes、user_properties都为空 type、value也不需要校验!")
                                else:
                                    print(str(i.get("user_properties")) + "未找到相同user_properties!")
                                    err_data.append('未发现此事件内的参数!事件信息:{}'.format(i.get("event")))
                        else:
                            print(str(i.get("attributes")) + "未找到相同attributes!")
                            err_data.append('未发现此事件内的参数!事件信息:{}'.format(i.get("event")))
                else:
                    print(str(i.get("event")) + "未找到相同event!")
                    err_data.append('未发现此事件的埋点信息!事件信息:{}'.format(i.get("event")))
            else:
                print("event不存在!")
        if len(event_data) < 1:
            all_data.append(' 埋点event信息错误!事件信息:{}'.format(i))
        elif len(attributes_data) < 1:
            all_data.append(' 埋点attributes信息错误!事件信息:{}'.format(i))
        elif len(user_properties_data) < 1:
            all_data.append(' 埋点user_properties信息错误!事件信息:{}'.format(i))
        elif len(type_data) < 1:
            all_data.append(' 埋点type信息错误!事件信息:{}'.format(i))
        elif len(value_data) < 1:
            all_data.append(' 埋点value信息错误!事件信息:{}'.format(i))
    err_data = np.array(err_data)
    all_data = np.array(all_data)
    print(all_data)
    return all_data