from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

sleep(3)

pageSource = driver.page_source

print(type(pageSource))

with open('/Users/liminkang/Desktop/pageSource.html', 'w', encoding='utf8') as f:
    data = driver.page_source
    f.write(data)
    # print(data)

driver.quit()


