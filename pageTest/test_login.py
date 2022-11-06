from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
import ddt

"""
用于测试登陆企业数字化分享平台的登陆功能
"""


@ddt.ddt
class TestLogin(unittest.TestCase):
    """
     测试准备前所做的操作
    """
    def setUp(self):
        test_url = 'http://192.168.0.68:9002/#/login'
        # 设置浏览器无界面启动
        self.chromeOption = webdriver.ChromeOptions()
        self.chromeOption.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chromeOption)
        self.driver.implicitly_wait(30)
        # 打开浏览器
        self.driver.get(test_url)

    """
    测试结束后所做的操作
    """
    def tearDown(self):
        self.driver.quit()

    """
    执行测试用例1-login
    """

    @ddt.data(['liminkang', 'A123456%', 0], ['liminkang', 'a123456%', 1])
    @ddt.unpack
    def test_001_login(self, account, password, status):
        # 账号输入框
        self.accountInput = self.driver.find_element(By.ID, "custom-validation_userName")
        print(self.accountInput)
        self.accountInput.clear()
        self.accountInput.send_keys(account)
        time.sleep(1)

        # 密码输入框
        self.passwordInput = self.driver.find_element(By.ID, "custom-validation_password")
        print(self.passwordInput)
        self.passwordInput.clear()
        self.passwordInput.send_keys(password)
        time.sleep(1)

        # 点击确认按钮
        self.submit = self.driver.find_element(By.XPATH, "//button[contains(@class, 'login-doit') and @type = 'submit']")
        self.submit.click()

        # 判断是否登陆成功
        if status == 0:
            # 用户名或密码不正确
            self.assertIn('用户名或密码不正确。', self.driver.page_source)
        if status == 1:
            # 成功登陆
            self.name = self.driver.find_element(By.XPATH, "//div[contains(@class, 'tool-popover')]/div[@class='name']")
            print(self.name.text)
            self.assertEqual(self.name.text, "LiMinKang")
            

if __name__ == '__main__':
    unittest.main()






