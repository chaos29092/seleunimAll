# 抓取阿里巴巴国际站的所有类目
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://m.alibaba.com/Categories")
driver.maximize_window()
time.sleep(2)

with open('data', 'w') as f:
    for text in driver.find_elements_by_xpath("//div[@level='1']/ul/li/a"):
        f.write(text.text+"\n")

    url1=[]
    url2=[]
    url3=[]
    for menu1 in driver.find_elements_by_xpath("//ul/li/a[@class='entry']"):
        url1.append(menu1.get_attribute('href'))

    for url in url1:
        driver.get(url)
        for menu2 in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a[@class="entry"]'):
            url2.append(menu2.get_attribute('href'))
        for keyword in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a'):
            f.write(keyword.text + "\n")

    for url in url2:
        driver.get(url)
        for menu3 in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a[@class="entry"]'):
            url3.append(menu3.get_attribute('href'))
        for keyword in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a'):
            f.write(keyword.text + "\n")

    for url in url3:
        driver.get(url)
        for menu4 in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a[@class="entry"]'):
            url3.append(menu4.get_attribute('href'))
        for keyword in driver.find_elements_by_xpath('//div[@level="1"]/ul/li/a'):
            f.write(keyword.text + "\n")

    print(url2)

time.sleep(2)

driver.quit()
