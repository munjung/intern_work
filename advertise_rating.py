from selenium import webdriver
import pymysql
import pandas as pd
import time
from tqdm import tqdm
import os

path = '/Users/mycelebs/Desktop/advertiser_data.xlsx'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/mycelebs/Downloads/chromedriver')
url = input('홈페이지 주소입력')
driver.get(str(url))
alert = driver.switch_to_alert()
alert.accept()
driver.find_element_by_css_selector('#adminId').send_keys('admin')
driver.find_element_by_css_selector('#adminPw').send_keys('admin')
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()

advertiser_update = pd.read_excel(path)

for idx, row in tqdm(advertiser_update.iterrows()):
	driver.get('http://dev.mycelebs.com/donut/Celeb/ShowManageCeleb?targetDataTable=advertiser_data')
	time.sleep(1)

	driver.find_element_by_css_selector('#s_ad_pk').clear() #solr query
	driver.find_element_by_css_selector('#s_ad_pk').send_keys(str(row['ad_pk']))

	driver.find_element_by_css_selector('#s_cd_solr_search').clear() #solr query
	driver.find_element_by_css_selector('#s_cd_solr_search').send_keys(str(row['cd_solr_search']))

	driver.find_element_by_css_selector('#s_cd_match_word').clear() #match word
	driver.find_element_by_css_selector('#s_cd_match_word').send_keys(str(row['cd_match_word']))

	driver.find_element_by_css_selector('#s_cd_similar_name').clear() #similar name
	driver.find_element_by_css_selector('#s_cd_similar_name').send_keys(str(row['cd_similar_name']))

	driver.find_element_by_css_selector('#s_ad_company_name').clear() #company name
	driver.find_element_by_css_selector('#s_ad_company_name').send_keys(str(row['ad_company_name']))

	driver.find_element_by_css_selector('#s_ad_business_type').clear() #businesss type
	driver.find_element_by_css_selector('#s_ad_business_type').send_keys(str(row['ad_business_type']))

	if pd.notnull(row['ad_company_address']):
		driver.find_element_by_css_selector('#s_ad_company_address').clear() #company adress
		driver.find_element_by_css_selector('#s_ad_company_address').send_keys(str(row['ad_company_address']))

	if pd.notnull(row['ad_tele_num']):
		driver.find_element_by_css_selector('#s_ad_tele_num').clear() #tele num
		driver.find_element_by_css_selector('#s_ad_tele_num').send_keys(str(row['ad_tele_num']))	

	if pd.notnull(row['ad_homepage_url']):
		driver.find_element_by_css_selector('#s_ad_homepage_url').clear() #hompage url
		driver.find_element_by_css_selector('#s_ad_homepage_url').send_keys(str(row['ad_homepage_url']))

	if pd.notnull(row['ad_instagram_url']):
		driver.find_element_by_css_selector('#s_ad_instagram_url').clear() #instagram url
		driver.find_element_by_css_selector('#s_ad_instagram_url').send_keys(str(row['ad_instagram_url']))

	if pd.notnull(row['ad_facebook_url']):
		driver.find_element_by_css_selector('#s_ad_facebook_url').clear() #facebook url
		driver.find_element_by_css_selector('#s_ad_facebook_url').send_keys(str(row['ad_facebook_url']))

	if pd.notnull(row['ad_youtube_query']):
		driver.find_element_by_css_selector('#s_ad_youtube_query').clear() #youtube url
		driver.find_element_by_css_selector('#s_ad_youtube_query').send_keys(str(row['ad_youtube_query']))

	driver.find_element_by_css_selector('div.row div:nth-of-type(2) div input.btn.btn-primary').click()  #추가하기 클

	alert = driver.switch_to_alert()
	alert.accept()

	time.sleep(1.5)

driver.close()



