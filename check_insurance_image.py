from selenium import webdriver
import pandas as pd
import time


insurance_excel = pd.read_excel('/Users/mycelebs/Desktop/보험/보험사.xlsx')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/mycelebs/Downloads/chromedriver')
driver.get('http://mycelebsTempUser:bx7a8s30FmDH@dev.mycelebs.com/donut/')
alert = driver.switch_to_alert()
alert.accept()
driver.find_element_by_css_selector('#adminId').send_keys('admin')
driver.find_element_by_css_selector('#adminPw').send_keys('admin')
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()

for idx, row in insurance_excel.iterrows():
	driver.get('http://dev.mycelebs.com/donut/CelebImage/ShowManage/'+str(row['cd_idx']))
	print(row['cd_idx'])
	time.sleep(1.5)
	
driver.close()
	
