import time
import os
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class driver():

    #driver初始化
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "juntao"
        caps["appPackage"] = "com.campro.livechat"
        caps["appActivity"] = "app.mvp.welcome.WelcomeActivity"
        caps["platformVersion"] = "11"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.action = TouchAction(self.driver)

    #坐标点击
    def tap(self, x, y):
        TouchAction(self.driver).tap(x=x, y=y).perform()
        time.sleep(0.5)

    #findById和wait等待封装
    def byId(self,arg):
        elementbyId = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(arg))
        time.sleep(1)
        return elementbyId

    #findByXpath和wait等待封装
    def byXpath(self,arg):
        elementbyxpath = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(arg))
        time.sleep(1)
        return elementbyxpath

    #返回元素列表和wait等待封装
    def sbyId(self,arg):
        elementsbyId = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(arg))
        time.sleep(0.5)
        return elementsbyId

    # 按钮倒计时结束后点击
    def clockover(self, arg):
        clock = self.driver.find_element_by_id(arg).text
        while clock != 'I got it':
            clock = self.driver.find_element_by_id(arg).text
            time.sleep(0.5)
        self.driver.find_element_by_id(arg).click()
        time.sleep(1)

    #多次点击id
    def clicksbyid(self,arg,times):
        for i in range(times):
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(arg)).click()
            time.sleep(1)

    # 多次点击xpath
    def clicksbyxpath(self,arg,times):
        for i in range(times):
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(arg)).click()
            time.sleep(1)

    #等待元素
    def show(self,arg):
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(arg))


    #截图
    def screenshot(self):
        now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file('/Users/edy/PycharmProjects/mw/Campro/img/'+now+'.png')


    #退出
    def quit(self):
        self.driver.quit()