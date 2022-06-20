# encoding=GBK
import time
import unittest
from common.drive import driver


class regwithgg(unittest.TestCase):

    dr = driver()

    def setUp(self):
        time.sleep(2)

    def test_01(self):
        '''进入到登录页'''
        try:
            self.dr.clicksbyid('com.android.permissioncontroller:id/permission_allow_button',2)
            self.dr.byId('com.campro.livechat:id/iv_dialog_first_policy_agree').click()
            self.dr.byId('com.campro.livechat:id/tv_dialog_first_policy_confirm').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView').click()
            self.dr.byId('com.campro.livechat:id/linearlayout_login_google').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout').click()
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("进入登录页异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('进入登录页成功')

    def test_02(self):
        '''邀请码'''
        try:
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText[1]').click()
            el = self.dr.sbyId('com.campro.livechat:id/item_code_1')
            # v = ['Y', 'D', 'Q', 'B', 'X']
            v = ['a', 'b', 'c', 'd', 'e']
            for i in range(len(el)):
                el[i].send_keys(v[i])
                time.sleep(0.5)
            self.dr.byId('com.campro.livechat:id/tv_confirm').click()
        except (AssertionError,Exception) as e:
            self.dr.screenshot()
            print("输入邀请码异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('输入邀请码成功')

    def test_03(self):
        '''输入昵称'''
        try:
            self.dr.byId('com.campro.livechat:id/et_name').click()
            self.dr.byId('com.campro.livechat:id/et_name').send_keys('testuser')
            self.dr.driver.hide_keyboard()
            self.dr.byId('com.campro.livechat:id/tv_save').click()
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("输入昵称异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('输入昵称成功')

    def test_04(self):
        '''选择年龄'''
        try:
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView').click()
            # self.dr.byId('com.campro.livechat:id/tv_save').click()
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("选择年龄异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('选择年龄成功')


    def test_05(self):
        '''上传照片'''
        try:
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]').click()
            self.dr.clockover('com.campro.livechat:id/tv_know')
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView').click()
            self.dr.byXpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.ImageView').click()
            self.dr.byId('com.campro.livechat:id/tv_upload_photos_confirm').click()
            self.dr.clicksbyid('com.campro.livechat:id/tv_photo_end',3)
            self.dr.byId('com.campro.livechat:id/tv_save').click()
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("上传照片异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('上传照片成功')

    def test_06(self):
        '''上传视频'''
        try:
            self.dr.byId('com.campro.livechat:id/jumpVideo').click()
            self.dr.clockover('com.campro.livechat:id/tv_know')
            self.dr.byId('com.campro.livechat:id/jumpVideo').click()
            self.dr.byId('com.campro.livechat:id/tv_allow').click()
            self.dr.clicksbyid('com.android.permissioncontroller:id/permission_allow_foreground_only_button',2)
            self.dr.tap(x='363', y='1239')
            self.dr.byId('com.campro.livechat:id/record_controller').click()
            self.dr.show('com.campro.livechat:id/record_again')
            self.dr.byId('com.campro.livechat:id/record_controller').click()
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("上传视频异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('上传视频成功')

    def test_07(self):
        '''等待审核'''
        try:
            text = self.dr.byId('com.campro.livechat:id/start_verify').text
            assert text=='Waiting For Review'
        except (AssertionError, Exception) as e:
            self.dr.screenshot()
            print("等待审核异常：{}".format(e))
            self.dr.quit()
            raise
        else:
            print('等待审核成功')

    def test_08(self):
        try:
            self.dr.quit()
        except Exception:
            print('Quit')


if __name__ == '__main__':
    unittest.main()