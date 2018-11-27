from selenium import webdriver
import pandas as pd
import time
from tqdm import tqdm
import os
import random 
import itertools
import numpy as np


os.chdir(r'/Users/mycelebs/Desktop/ExcitingL')


wine_url = "http://dev.mycelebs.com/donut/Vertical/FinderItem/525" #5
beer_url = "http://dev.mycelebs.com/donut/Vertical/FinderItem/1252" #3
webtoon_url = "http://dev.mycelebs.com/donut/Vertical/FinderItem/374" #4

urls = [wine_url, beer_url, webtoon_url]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='/Users/mycelebs/Downloads/chromedriver', chrome_options=chrome_options)

driver.get('http://mycelebsTempUser:bx7a8s30FmDH@dev.mycelebs.com/donut/')

alert = driver.switch_to_alert()
alert.accept()
input_id = input('id: ')
input_pw = input('pw: ')
driver.find_element_by_css_selector('#adminId').send_keys(str(input_id))
driver.find_element_by_css_selector('#adminPw').send_keys(str(input_pw))
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()




#################################################################################
###################################### 와인 ######################################
#################################################################################

driver.get(wine_url)

# 기존의 필터 지우고 저장
exist_btn_list = driver.find_elements_by_css_selector("#submit_item > p > span.glyphicon.glyphicon-remove._btn_delete")

for exist_btn in exist_btn_list:
    exist_btn.click()

driver.find_element_by_css_selector("#write > button").click()
time.sleep(0.5)


# 새로운 필터 랜덤 추출 
dev_btn_list = driver.find_elements_by_css_selector("body > div.container > div > div.cont_area > div > table > tbody > tr:nth-child(3) > td > p > button")
dev_btn_txt_list = [x.text for x in dev_btn_list]
print(dev_btn_txt_list)
dev_btn_id_list = [x.get_attribute("id") for x in dev_btn_list]
dev_btn_id_list
check = dev_btn_txt_list
time.sleep(1)
new_btn_list = np.random.choice(dev_btn_id_list, len(exist_btn_list), replace=False)    
new_btn_list


# 새로운 필터 저장 
new_wine_list = []
for btn in new_btn_list:
    time.sleep(1)
    button = driver.find_element_by_css_selector("#" + btn)
    new_wine_list.append(button.text)
    driver.execute_script("arguments[0].click();",button)
    add_button = driver.find_element_by_css_selector("#field_form > button")
    driver.execute_script("arguments[0].click();",add_button)

print('wine')
print(new_wine_list)
driver.find_element_by_css_selector("#write > button").click()




#################################################################################
###################################### 비어 ######################################
#################################################################################

driver.get(beer_url)

# 기존의 필터 지우고 저장
exist_btn_list = driver.find_elements_by_css_selector("#submit_item > p > span.glyphicon.glyphicon-remove._btn_delete")

for exist_btn in exist_btn_list:
    exist_btn.click()

driver.find_element_by_css_selector("#write > button").click()
time.sleep(0.5)


# 새로운 필터 랜덤 추출 
dev_btn_list = driver.find_elements_by_css_selector("body > div.container > div > div.cont_area > div > table > tbody > tr:nth-child(3) > td > p > button")
dev_btn_txt_list = [x.text for x in dev_btn_list]
print(dev_btn_txt_list)
dev_btn_id_list = [x.get_attribute("id") for x in dev_btn_list]
dev_btn_id_list
check = dev_btn_txt_list
time.sleep(1)
new_btn_list = np.random.choice(dev_btn_id_list, len(exist_btn_list), replace=False)    
new_btn_list


# 새로운 필터 저장 
new_beer_list = []
for btn in new_btn_list:
    time.sleep(1)
    button = driver.find_element_by_css_selector("#" + btn)
    new_beer_list.append(button.text)
    driver.execute_script("arguments[0].click();",button)
    add_button = driver.find_element_by_css_selector("#field_form > button")
    driver.execute_script("arguments[0].click();",add_button)

print('beer')
print(new_beer_list)
driver.find_element_by_css_selector("#write > button").click()




#################################################################################
###################################### 웹툰 ######################################
#################################################################################

driver.get(webtoon_url)

# 기존의 필터 지우고 저장
exist_btn_list = driver.find_elements_by_css_selector("#submit_item > p > span.glyphicon.glyphicon-remove._btn_delete")
exist_btn_list = exist_btn_list[1:]

for exist_btn in exist_btn_list:
    exist_btn.click()

driver.find_element_by_css_selector("#write > button").click()
time.sleep(0.5)


# 새로운 필터 랜덤 추출 
dev_btn_list = driver.find_elements_by_css_selector("body > div.container > div > div.cont_area > div > table > tbody > tr:nth-child(3) > td > p > button")
dev_btn_txt_list = [x.text for x in dev_btn_list]
#print(dev_btn_txt_list)
dev_btn_id_list = [x.get_attribute("id") for x in dev_btn_list]
dev_btn_id_list
check = dev_btn_txt_list
time.sleep(1)
new_btn_list = np.random.choice(dev_btn_id_list, len(exist_btn_list), replace=False)    
new_btn_list


# 새로운 필터 저장 
new_webtoon_list = []
for btn in new_btn_list:
    time.sleep(1)
    button = driver.find_element_by_css_selector("#" + btn)
    new_webtoon_list.append(button.text)
    driver.execute_script("arguments[0].click();",button)
    add_button = driver.find_element_by_css_selector("#field_form > button")
    driver.execute_script("arguments[0].click();",add_button)

print('webtoon')
print(new_webtoon_list)
driver.find_element_by_css_selector("#write > button").click()



driver.close()


####################################################################################
###################################### 파일 저장 #####################################
####################################################################################

new_filter_list = [new_wine_list, new_beer_list, new_webtoon_list]
wine_str = ",".join(new_wine_list)
beer_str = ",".join(new_beer_list)
webtoon_str = ",".join(new_webtoon_list)

df = pd.DataFrame({"wine":[wine_str], "beer":[beer_str], "webtoon":[webtoon_str]})
date = time.strftime("%y%m%d")
df.to_excel('/Users/mycelebs/Desktop/ExcitingL/weekly_filter/' + date + "_weekly_filter.xlsx")

