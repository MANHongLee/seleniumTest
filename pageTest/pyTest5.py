from selenium import webdriver
from time import sleep

'''
1、测试当前浏览器窗口的具柄，以及为数组时，下标为0先开始；
2、测试新建一个tab/window窗口，发现是记录为打开浏览器驱动时的所记录的所有窗口的具柄；
'''
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(3)
curHandls = driver.current_window_handle
print(curHandls)
driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
driver.get('https://www.baidu.com')
countHandls = driver.window_handles
print(countHandls)

driver.quit()