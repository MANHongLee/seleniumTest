from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import hashlib
'''
尝试使用谷歌浏览器进行input下拉选择，打开本地文件路径需要添加file:///
'''
htmlUrl = 'file:///' + 'Users'+os.sep+'liminkang'+os.sep+'vscodeProjects'+os.sep+'htmlTest'+os.sep+'test'+os.sep+'test10.html'
fileURl = os.sep+'Users'+os.sep+'liminkang'+os.sep+'vscodeProjects'+os.sep+'htmlTest'+os.sep+'test'+os.sep+'test10.html'

# print(htmlUrl)
# driver = webdriver.Chrome()
# action = ActionChains(driver)
# driver.get(htmlUrl)
#
# sleep(1)
# ele = driver.find_element(By.ID, 'select')
# ele.click()
#
# sleep(1)
# ele.send_keys('b')
# # 向下点击
#
# action.key_down(Keys.DOWN, ele).perform()
# sleep(1)
# ele.send_keys(Keys.ENTER)
# sleep(3)

'''
尝试复制、粘贴的操作
'''
# input1 = driver.find_element(By.ID, 'input1')
# input1.send_keys('abcdefghijklnm')
# sleep(1)
# action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND)
# action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND)
# action.perform()
# sleep(1)
# input2 = driver.find_element(By.ID, 'input2')
# input2.click()
# sleep(1)
# action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND)
# action.perform()
# sleep(2)
#
# driver.quit()

'''
测试prompt弹框的使用
'''
# driver = webdriver.Chrome()
# driver.get(htmlUrl)
# b1 = driver.find_element(By.ID, 'b2')
# # 打开弹框
# b1.click()
# print(driver.switch_to.alert.text)
# sleep(2)
# driver.switch_to.alert.send_keys('input your name...')
# sleep(2)
# # 点击弹框确定按钮
# driver.switch_to.alert.accept()
# sleep(1)
# one = driver.find_element(By.ID, 'one')
# # 打印输入框内的文字
# print(one.get_attribute('value'))
# sleep(1)
#
# driver.quit()

'''
获取文件的MD5值
'''


def get_md5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code


if __name__ == '__main__':
    print(get_md5(fileURl))
