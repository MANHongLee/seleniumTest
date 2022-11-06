from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time
import test_functions
import random


class TestCreatUnitOfCustomer(unittest.TestCase):
    def setUp(self):
        self.test_url = 'http://192.168.0.68:9002/#/login'

        # 设置填入的内容
        self.test_data = "{}单位客户{}".format(time.strftime("%m%d", time.localtime(time.time())), str(
            int(time.time()))[7:])

        # 设置浏览器无界面启动
        # self.chromeOption = webdriver.ChromeOptions()
        # self.chromeOption.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=self.chromeOption)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

        # 打开浏览器
        self.driver.get(self.test_url)

        # 账号输入框
        self.accountInput = self.driver.find_element(By.ID, "custom-validation_userName")
        # print(self.accountInput)
        self.accountInput.clear()
        self.accountInput.send_keys("liminkang")
        time.sleep(1)

        # 密码输入框
        self.passwordInput = self.driver.find_element(By.ID, "custom-validation_password")
        # print(self.passwordInput)
        self.passwordInput.clear()
        self.passwordInput.send_keys("a123456%")
        time.sleep(1)

        # 点击确认按钮
        self.submit = self.driver.find_element(By.XPATH,
                                               "//button[contains(@class, 'login-doit') and @type = 'submit']")
        self.submit.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    """
    测试新建单位客户
    """
    def test_002_creatsuc(self):

        # 进入到单位客户页
        self.driver.find_element(By.XPATH, "//a[text() = ' 前往商机管理系统 ']").click()
        time.sleep(2)
        self.driver.get("http://192.168.0.68:9002/#/message-database/customer-unit")
        time.sleep(3)

        # 点击添加按钮
        self.addButton = self.driver.find_element(By.XPATH, "//span[text() = '添加']")
        # print(self.addButton)
        self.addButton.click()
        time.sleep(5)

        # 页面跳转至单位客户录入页，定位各个必填项输入框，填入内容信息
        # 输入单位客户名称
        self.unit_customer_name = self.driver.find_element(By.ID, "name")
        self.unit_customer_name.clear()
        self.unit_customer_name.send_keys(self.test_data)

        # 输入联系方式
        self.callWay = self.driver.find_element(By.ID, "callWay")
        self.callWay.clear()
        self.callWay.send_keys(test_functions.get_mobile_number())

        # 输入公司地址
        self.address = self.driver.find_element(By.ID, "address")
        self.address.clear()
        self.address.send_keys(self.test_data)

        # 填入行政区划
        self.nativePlaceCodeList = self.driver.find_element(By.ID, "nativePlaceCodeList")
        self.driver.execute_script("arguments[0].click();", self.nativePlaceCodeList)
        # self.nativePlaceCodeList.click()
        self.firstList = self.driver.find_elements(By.XPATH, "//ul[@class = 'ant-cascader-menu'][1]/li")
        self.firstaddress = self.driver.find_element(By.XPATH, "//ul[@class = 'ant-cascader-menu'][1]/li[" + str(
            random.randint(0, len(self.firstList))) + "]")
        self.firstaddress.click()
        time.sleep(1)
        self.secondList = self.driver.find_elements(By.XPATH, "//ul[@class = 'ant-cascader-menu'][2]/li")
        self.secondaddress = self.driver.find_element(By.XPATH, "//ul[@class = 'ant-cascader-menu'][2]/li["+str(
            random.randint(0, len(self.secondList)))+"]")
        self.secondaddress.click()
        time.sleep(2)
        self.thirdList = self.driver.find_elements(By.XPATH, "//ul[@class = 'ant-cascader-menu'][3]/li")
        self.thirdaddress = self.driver.find_element(By.XPATH, "//ul[@class = 'ant-cascader-menu'][3]/li["+str(
            random.randint(0, len(self.thirdList)))+"]")
        # print(self.thirdaddress)
        self.thirdaddress.click()
        # time.sleep(10)

        # 填入所属行业
        self.industry_involved = self.driver.find_elements(By.XPATH, "//div[@class = 'ant-select-selector']")
        self.industry_involved[0].click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN, self.industry_involved[0]).perform()
        ActionChains(self.driver).key_down(Keys.ENTER, self.industry_involved[0]).perform()

        # 输入客户来源
        # self.industry_involved = self.driver.find_elements(By.XPATH, "//div[@class = 'ant-select-selector']")
        self.industry_involved[1].click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN, self.industry_involved[1]).perform()
        ActionChains(self.driver).key_down(Keys.ENTER, self.industry_involved[1]).perform()

        # 输入备注
        self.remark = self.driver.find_element(By.XPATH, "//textarea[@id = 'remark']")
        self.remark.send_keys(self.test_data)

        # 点击确定
        time.sleep(10)
        self.commitBtn = self.driver.find_element(By.XPATH, "//button[@type = 'button']/span[text() = '确 定']")
        self.commitBtn.click()
        time.sleep(10)

        # 点击取消
        # time.sleep(10)
        # self.cancelBtn = self.driver.find_element(By.XPATH, "//button[@type = 'button']/span[text() = '取 消']")
        # self.cancelBtn.click()


if __name__ == '__main__':
    unittest.main()




