from selenium import webdriver
import pymysql
import pandas as pd
import time
from tqdm import tqdm
import os
import requests
from bs4 import BeautifulSoup

lotte = pd.read_excel("/Users/mycelebs/Downloads/hmr_롯데_요리하다.xlsx")
lotte = lotte[lotte["check"]==1]
lotte.head()
menu_url = list(lotte["url"])
name_list = list(lotte["prod-name"])


os.chdir("/Users/mycelebs/Desktop/LOTTEMART")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=chrome_options)

# 상품별 리뷰 페이지
page_list = []


for menu in tqdm(menu_url):
	driver.get(menu)
	try:
		pages = int(driver.find_element_by_xpath('//*[@id="pagingDiv"]/div/a[2]').get_attribute("title").split(" 페이지")[0])
		page_list.append(pages)
		print(pages, "pages")
	except:
		try:
			t = driver.find_elements_by_css_selector('#pagingDiv > div > span > a')
			pages = [x.text for x in t][-1]
			page_list.append(pages)
			print(pages, "pages")
		except:
			page_list.append(1)
			print(1, "pages")
	
driver.close()

len(menu_url)
len(page_list)
len(name_list)



final_df = pd.DataFrame()
# 40 
# 40 ~ 80 
# 80 ~ 13
for i in tqdm(range(80, 134)):
	
	prodCd = menu_url[i].split("CD=")[1]
	pages = int(page_list[i])

	if prodCd == 'D000003067473':
		continue

	if prodCd == 'D000002948000':
		continue

	if prodCd == 'D000002908372':
		continue

	df = pd.DataFrame()
	for page in tqdm(range(pages)):
		page = page + 1
		url = 'http://www.lottemart.com/product/ajax/ProductReview.do?searchFilter=0&orderFilter=dateOrder&page={}&prodCd={}&prodTypeNm=all&ProdLinkKindCd=&CAT_CD_YN=N&chgReviewCnt=Y'.format(page, prodCd)

		source_code = requests.get(url).text
		soup = BeautifulSoup(source_code, "lxml")

		#score
		score_tag = soup.find_all("span", class_="ico-star-type1")
		score = [x.get_text().split(" /")[0][1:] for x in score_tag]

		#comment
		comment_tag = soup.find_all("td", class_="subject")
		comment = [x.get_text() for x in comment_tag]

		#comment2
		comment2_tag = soup.find_all("div", class_="faq-comm")
		comment2 = [x.get_text().replace("\t", "").replace("\r", "").replace("\n", "") for x in comment2_tag]

		#price
		price_tag = soup.find_all("p", class_="sfaction-price")
		price = [x.get_text().replace("\t", "").replace("\r", "").replace("\n", "").replace("가격", "") for x in price_tag]

		#delivery
		del_tag = soup.find_all("p", class_="sfaction-del")
		delivery = [x.get_text().replace("\t", "").replace("\r", "").replace("\n", "").replace("배송", "") for x in del_tag]

		#quality 
		qual_tag = soup.find_all("p", class_="sfaction-qual")
		quality = [x.get_text().replace("\t", "").replace("\r", "").replace("\n", "").replace("품질", "") for x in qual_tag]


		temp = pd.DataFrame()
		temp["score"] = score
		temp["comment"] = comment
		temp["comment2"] = comment2
		temp["price"] = price
		temp["delivery"] = delivery
		temp["quality"] = quality
		temp["name"] = name_list[i]
		df = pd.concat([df, temp])

	final_df = pd.concat([final_df, df])

final_df.to_excel("lottemart_v3.xlsx")


os.chdir("/Users/mycelebs/Desktop/LOTTEMART")
v1 = pd.read_excel("lottemart_v1.xlsx")
v2 = pd.read_excel("lottemart_v2.xlsx")
v3 = pd.read_excel("lottemart_v3.xlsx")


final = pd.concat([v1, v2, v3])
final.to_excel("final.xlsx")



##################################################################
####################### 롯데마트 이미지 가져오기 #######################
##################################################################

lotte = pd.read_excel("/Users/mycelebs/Downloads/hmr_롯데_요리하다.xlsx")
lotte = lotte[lotte["check"]==1]
menu_url = list(lotte["url"])
name_list = list(lotte["prod-name"])
prodCd = list(lotte["prod-cd"])

image_list = []

for url in tqdm(menu_url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--incognito')
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(url)
	try:
		image = driver.find_element_by_xpath('//*[@id="imgBigSize"]').get_attribute('src')
		image_list.append(image)
		driver.close()
	except:
		image_list.append(np.nan)
		driver.close()

os.chdir("/Users/mycelebs/Desktop/LOTTEMART")
image_df = pd.DataFrame({"prodCd" : prodCd, "name" : name_list, "menu" : menu_url, "image_url" : image_list})
image_df.to_excel("lottemart_image.xlsx")



##################################################################
####################### 롯데마트 이미지 다운로드 #######################
##################################################################


from PIL import Image
from tqdm import tqdm
import os
import pandas as pd
import urllib.request

data = image_df

error_list = []
os.chdir("/Users/mycelebs/Desktop/LOTTEMART/image")
for i in tqdm(range(len(data))):
    try:
        src = str(data["image_url"].iloc[i])
        file_name = str(data["prodCd"].iloc[i])
        print(i, file_name)
        urllib.request.urlretrieve(src, file_name+".jpg")

        img = Image.open(file_name + ".jpg")  # image extension *.png,*.jpg
        new_width = 500
        new_height = 500
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img = img.convert('RGB')
        img.save(file_name + ".jpg")
    except:
        error_list.append(file_name)



url = 'http://m.lottemart.com/mobile/cate/PMWMCAT0004_New.do?ProductCD=8801118000881&CategoryID=C20200040003&SITELOC='
source_code = requests.get(url).text
source_code 
soup = BeautifulSoup(source_code, "lxml")
soup.find_all("img")
soup.find_all('ul', class_='swiper-wrapper')[0].find('img')['src']
