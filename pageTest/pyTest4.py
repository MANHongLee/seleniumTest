from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
模拟鼠标悬浮
'''

driver = webdriver.Chrome()

driver.get('https://sahitest.com/demo/mouseover.htm')

sleep(3)

ele = driver.find_element(By.XPATH, '//div/div')

sleep(3)

ActionChains(driver).move_to_element(ele).perform()

sleep(3)

driver.quit()

