from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

sleep(3)

curSize = driver.get_window_size()

print(curSize)

sleep(3)

driver.set_window_size(800, 900)

sleep(3)

driver.quit()

