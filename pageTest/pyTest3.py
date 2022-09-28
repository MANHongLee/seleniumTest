from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
'''
模拟按下command键，点击链接
'''
driver = webdriver.Chrome()

driver.get('https://sahitest.com/demo/clickCombo.htm')

sleep(3)

ele = driver.find_element(By.XPATH, '//div/div')

sleep(3)

# 针对ele元素按住command键
ActionChains(driver).key_down(Keys.COMMAND).perform()

ele.click()

sleep(3)

driver.quit()

