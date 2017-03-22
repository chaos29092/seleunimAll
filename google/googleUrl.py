#利用关键词抓取ad和一般website
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pymongo import MongoClient

client = MongoClient()
db = client.google

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.google.com/ncr")
driver.maximize_window()
time.sleep(2)

with open('keywords_1', 'r') as f:
    for line in f.readlines():
        driver.find_element_by_xpath('//input[@id="lst-ib"]').send_keys(line.strip()+"china -filetype:pdf -india -b2b -marketplace -leads -platform -directory -connecting -\"find suppliers\" -\"find manufacturers\" -member -buyers  -forum -\"yellow pages\" -yellowpages -online -shop -store -blog -wikipedia -youtube -.edu -.gov")
        driver.find_element_by_xpath('//input[@id="lst-ib"]').send_keys(Keys.ENTER)

        try:
            urls = driver.find_elements_by_xpath('//a[@data-preconnect-urls]').get_attribute('data-preconnect-urls')
        except:
            pass


