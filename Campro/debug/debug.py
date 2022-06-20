# encoding=GBK
import time
import unittest
from Campro.common.drive import driver


class regwithgg(unittest.TestCase):

    dr = driver()
    # skip = 0

    def setUp(self):
        time.sleep(1.5)

    def test_01(self):
        '''进入到登录页'''
        try:
            self.dr.clicksbyid('com.android.permissioncontroller:id/permission_allow_button',2)
            self.dr.byId('com.campro.livechat:id/iv_dialog_first_policy_agree').click()
            self.dr.byId('com.campro.livechat:id/tv_dialog_first_policy_confirm1').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView').click()
            self.dr.byId('com.campro.livechat:id/linearlayout_login_google').click()
            assert self.dr.byId('com.campro.livechat:id/linearlayout_login_google').text() == 'yes'
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout').click()
        except (AssertionError,Exception) as e:
            self.dr.screenshot()
            print("进入登录页异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('进入登录页成功')

    # @unittest.skipIf(skip==1,'skip this test')
    def test_02(self):
        '''邀请码'''
        self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText[1]').click()
        el = self.dr.sbyId('com.campro.livechat:id/item_code_1')
        v = ['a', 'b', 'c', 'd', 'e']
        for i in range(len(el)):
            el[i].send_keys(v[i])
            time.sleep(0.5)
        self.dr.byId('com.campro.livechat:id/tv_confirm').click()

    # @unittest.skip
    def test_03(self):
        '''输入昵称'''
        self.dr.byId('com.campro.livechat:id/et_name').click()
        self.dr.byId('com.campro.livechat:id/et_name').send_keys('testuser')
        self.dr.driver.hide_keyboard()
        self.dr.byId('com.campro.livechat:id/tv_save').click()
    #
    # def test_04(self):
    #     '''选择年龄'''
    #     self.dr.byId('com.campro.livechat:id/tv_save').click()
    #
    # def test_05(self):
    #     '''上传照片'''
    #     self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]').click()
    #     self.dr.clockover('com.campro.livechat:id/tv_know')
    #     self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]').click()
    #     self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView').click()
    #     self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView').click()
    #     self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.ImageView').click()
    #     self.dr.byId('com.campro.livechat:id/tv_upload_photos_confirm').click()
    #     self.dr.clicksbyid('com.campro.livechat:id/tv_photo_end',3)
    #     self.dr.byId('com.campro.livechat:id/tv_save').click()
    #
    # def test_06(self):
    #     '''上传视频'''
    #     self.dr.byId('com.campro.livechat:id/jumpVideo').click()
    #     self.dr.clockover('com.campro.livechat:id/tv_know')
    #     self.dr.byId('com.campro.livechat:id/jumpVideo').click()
    #     self.dr.byId('com.campro.livechat:id/tv_allow').click()
    #     self.dr.clicksbyid('com.android.permissioncontroller:id/permission_allow_foreground_only_button',2)
    #     # self.dr.byId('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
    #     # self.dr.byId('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
    #     self.dr.tap(x='363', y='1239')
    #     self.dr.byId('com.campro.livechat:id/record_controller').click()
    #     self.dr.show('com.campro.livechat:id/record_again')
    #     self.dr.byId('com.campro.livechat:id/record_controller').click()
    #
    # def test_07(self):
    #     '''等待审核'''
    #     text = self.dr.text('com.campro.livechat:id/start_verify')
    #     assert text=='I got it'
    #
    # def test_08(self):
    #     pass


if __name__ == '__main__':
    unittest.main(failfast=True)