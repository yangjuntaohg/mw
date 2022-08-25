import os


'''
手动触发埋点事件，完成操作后，将打点日志文件pull出来
'''

class AdbTools(object):
    def __int__(self, device_id='device_id', local_ptah='locat_json_path', device_path='device_json_path', packname="", grammar="ls", times=1,
     video_name="demo",
     new_tcp=5000, old_tcp=8000, text="default",
     new_x=1, new_y=1, old_x=2, old_y=2, keyevent="home", **kwargs):
        """
         :param device_id: 设备ID
         :param local_ptah: 本地路径
         :param device_path: 设备路径
         :param packname: 包名
         :param grammar: 语法
         :param times: 时间
         :param video_name: 名字
         :param new_tcp: 新的ip
         :param old_tcp: 当前ip
         :param text: 文本
         :param new_x: 期望坐标x
         :param new_y: 期望坐标y
         :param old_x: 当前坐标x
         :param old_y: 当前坐标y
         :param keyevent: 设备按键
         :return:
        """
        self.device_id = device_id
        self.local_ptah = local_ptah
        self.device_path = device_path
        self.packname = packname
        self.grammar = grammar
        self.times = times
        self.video_name = video_name
        self.new_tcp = new_tcp
        self.old_tcp = old_tcp
        self.text = text
        self.new_x = new_x
        self.new_y = new_y
        self.old_x = old_x
        self.old_y = old_y
        self.keyevent = keyevent

    @classmethod
    def get_device(cls):
        """
        查看连接设备
        :return:
        """
        devices = os.popen(r"adb devices")
        # print(devices.read())
        return devices.read()

    def get_state(self):
        """
         获取设备状态
         :return:
         """
        out, info = subprocess.getstatusoutput("adb -s {} get-stat".format(self.device_id))
        print(out, info)
        return info

    def adb_push(self):
        """
         向设备中复制文件
         :return:
         """
        push = os.popen(r"adb -s {} push {}".format(self.device_id, self.local_ptah, self.device_path))
        print(push.read())
        return push.read()

    def adb_pull(self):
        """
        从设备中复制文件
        :return:
        """
        # print(self.device_id, self.device_path, self.local_ptah)
        pull = os.popen(r"adb -s {} pull {} {}".format(self.device_id, self.device_path, self.local_ptah))
        print(pull.read())
        return pull.read()

    def adb_install(self):
        """
        adb 安装apk
        :return:
        """
        install = os.popen(r"adb -s {} install {}".format(self.device_id, self.packname))
        print(install.read())
        return install.read()


    '''
    因为打点日志文件按时间动态命名，无法精准pull最新生成的打点日志文件，所以需要将整个文件夹pull出来再对文件进行排序取最新日志文件
    '''
    def get_file_name(json_path):
        dir_list = os.listdir(json_path)
        if not dir_list:
            print("dir_list is None!")
            return
        else:
        try:
            exists_dir = os.path.exists(json_path + "/temp")
            if exists_dir:
                shutil.rmtree(json_path + "/temp")
                print("把temp文件夹删除!")
        except Exception as e:
            s = sys.exc_info()
            print("报错文件：{}\n报错行数：{}\n报错内容：{}".format(__file__, s[2].tb_lineno, e))
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间


        dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(json_path, x)))
        print(dir_list)
        file_name = "/" + dir_list[-1]
        print(file_name)
        return file_name