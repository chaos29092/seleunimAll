# 从adwords获取谷歌搜索量和点击费用，谷歌老封，失败

from selenium import webdriver
import time
from pymongo import MongoClient

client = MongoClient()
db = client.alibaba

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://adwords.google.com/ko/KeywordPlanner/Home")
driver.maximize_window()
time.sleep(2)

#login
driver.find_element_by_xpath('//div[@id="header-links"]/a').click()
driver.find_element_by_xpath('//input[@id="Email"]').send_keys('chinakejiafurnace@gmail.com')
driver.find_element_by_xpath('//input[@id="next"]').click()
driver.find_element_by_xpath('//input[@id="Passwd"]').send_keys('xRQCmp5cyWLFw7gi')
driver.find_element_by_xpath('//input[@id="signIn"]').submit()

keywords = ""
#search
for num in range(100):
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//div[@id="gwt-debug-splash-panel-stats-selection-input"]').click()

    if not keywords:
        for n in range(30):
            keywords = db.keywords.find_one_and_update({'done': {'$exists': False}}, {'$set': {'done': True}})[
                           'keyword'] + '\n' + keywords

    driver.find_element_by_xpath('//textarea[@id="gwt-debug-upload-text-box"]').send_keys(keywords)
    driver.find_element_by_xpath('//span[@id="gwt-debug-upload-ideas-button-content"]').click()


    try:
        driver.find_element_by_xpath('//div[@id=\"gwt-debug-column-KEYWORD-row-0-0\"]/div/span')
        #crawl
        for n in range(30):
            try:
                driver.implicitly_wait(0.01)
                keyword = driver.find_element_by_xpath('//div[@id=\"gwt-debug-column-KEYWORD-row-'+str(n)+'-0\"]/div/span').text
            except:
                pass

            try:
                monthSearch = driver.find_element_by_xpath('//div[@id=\"gwt-debug-column-SEARCH_VOLUME_PRIMARY-row-'+str(n)+'-0\"]').text
            except:
                pass

            try:
                price = 0
                price = driver.find_element_by_xpath('//div[@id=\"gwt-debug-column-SUGGESTED_BID-row-'+str(n)+'-2\"]/div').text
                if not price==0:
                    price = price[2:]
            except:
                pass

            try:
                db.keywordsPPC.insert_one({'keyword': keyword,'monthSearch':monthSearch,'price':price})
            except:
                pass


        driver.refresh()
        keywords = ""
    except:
        driver.refresh()




# driver.quit()
