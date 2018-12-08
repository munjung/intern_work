# 경로 C:/Users/mycelebs/work/Code_mycelebs_/tv_update/

# 기본정보 업데이트하기

# filePath = input('파일의 경로를 입력하세요 (ex: "/Users/KUK/)" ')

## solr_query Error 확인(임시)
import pandas as pd
import pymysql
import requests
import time
from tqdm import tqdm
import urllib.request

file_path = '/Users/mycelebs/Desktop/방송/18-10-18_회차별출연진.xlsx' #엑셀 파일 경로

sheets = pd.ExcelFile(file_path)
df = sheets.parse(1) #두번째 시트
df_short = df[['sub_cd_idx', 'cd_idx', 'solr_query']]

solr_list = df_short['solr_query']
r = requests.Session()

for idx, row in tqdm(df_short.iterrows()):
	query = df_short['solr_query'][idx]
	response = r.get(f'http://ba_search_replica.mycelebs.com:9100/solr-4.8.1/ba_crawl/select?q={query}&wt=json&indent=true')
	if response.status_code != 200:
		print(str(df_short['sub_cd_idx'][idx])+' / '+str(df_short['cd_idx'][idx])+' / '+str(df_short['solr_query'][idx]))
	time.sleep(0.5)

#### original code start
# os.chdir(filePath)
import time
import random
import os
# os.chdir('/Users/kuk/Library/Mobile Documents/com~apple~CloudDocs/python_code_zip/startup')
# os.chdir('/Users/jongwoo/mcs/MANAGE/program_data_update')
os.chdir('/Users/mycelebs/Desktop/방송')
%run 06_def_tv_zip




#os.chdir('/Users/kuk/Library/Mobile Documents/com~apple~CloudDocs/mycelebs/jtbc/관리')
# os.chdir('/Users/jongwoo/mcs/MANAGE/program_data_update')


fileName = input('회차정보 엑셀 파일명을 입력하세요. ')
# fileName_celeb = input('회차별출연진정보 엑셀 파일명을 입력하세요. ') yy-mm-dd

xls = pd.ExcelFile( fileName +'_회차정보업데이트.xlsx')
# xls_celeb = pd.ExcelFile( fileName_celeb +'.xlsx')
# xls_celeb = pd.ExcelFile( fileName +'_회차별출연진.xlsx')
tv_epi_info_df = xls.parse('시청률')
tv_epi_info_df = xls.parse(xls.sheet_names[1])



# tv_epi_info_df.to_excel('test.xlsx')

# r'C:/Users/Emily/Downloads/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='/Users/mycelebs/Downloads/chromedriver')
# driver=webdriver.Firefox()
pid = 'mycelebsTempUser'
ppw = 'bx7a8s30FmDH'
driver.get(f'http://{pid}:{ppw}@dev.mycelebs.com/donut/')

alert = driver.switch_to_alert()
alert.accept()




#adminId
driver.find_element_by_css_selector('#adminId').send_keys('admin')
driver.find_element_by_css_selector('#adminPw').send_keys('admin')
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()

# 1. 에피소드 관리
for i in range(len(tv_epi_info_df)):
    # if pd.to_datetime(time.strftime('%Y-%m-%d')) >= pd.to_datetime(tv_epi_info_df.epi_date[i]):
    if time.strftime('%Y-%m-%d') >= tv_epi_info_df.epi_date[i]:
        cd_idx = list(tv_epi_info_df.cd_idx)[i]
        check_url = 'http://dev.mycelebs.com/donut/Celeb/ShowManageTvCeleb?targetDataTable=tv_episode_info&cd_idx='+str(cd_idx)
        driver.get(check_url)
        r = driver.page_source
        soup = BeautifulSoup(r,'lxml')
        css_selector_date = 'body > div.container > div > div > form > div:nth-child(3) > input'
        css_selector_date_str = 'body > div.container > div > div > form > div:nth-child(4) > input'
        css_selector_date_rate = 'body > div.container > div > div > form > div:nth-child(5) > input'
        css_selector_naver_search_count = 'body > div.container > div > div > form > div:nth-child(6) > input'
        css_selector_2049_view_rate = 'body > div.container > div > div > form > div:nth-child(7) > input'
        css_selector_pay_per_view_rate = 'body > div.container > div > div > form > div:nth-child(8) > input'

        try:
            pre_date_and_pk_dict = {soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[2].text : soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[0].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))}
            pre_date =[soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[2].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))]
            pk_num_list = [soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[0].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))]
            # tv_epi_info_admin_url = 'http://skyfall.mycelebs.com:8000/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_info&cd_idx='+str(cd_idx)
            # driver.get(tv_epi_info_admin_url)

            if not str(list(tv_epi_info_df.epi_date)[i]) in pre_date:

                # tv_epi_info_admin_url = 'http://skyfall.mycelebs.com:8000/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_info&cd_idx=' + str(
                #     cd_idx)
                # driver.get(tv_epi_info_admin_url)
                driver.find_element_by_css_selector(css_selector_date).send_keys(list(tv_epi_info_df.epi_date)[i])
                driver.find_element_by_css_selector(css_selector_date_str).send_keys(list(tv_epi_info_df.epi_num)[i])
                driver.find_element_by_css_selector(css_selector_date_rate).send_keys(str(list(tv_epi_info_df.view_rate)[i]))
                #### 가짜 데이터 입력
                driver.find_element_by_css_selector(css_selector_naver_search_count).send_keys("0")
                driver.find_element_by_css_selector(css_selector_2049_view_rate).send_keys("0")
                driver.find_element_by_css_selector(css_selector_pay_per_view_rate).send_keys("0")
                ####

                btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
                btn.click()

                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(2)
            else:
                print(str(list(tv_epi_info_df.epi_date)[i]),'=',pre_date[pre_date.index(str(list(tv_epi_info_df.epi_date)[i]))])
                edit_url ='http://dev.mycelebs.com/donut/Celeb/UpdateManageTvCeleb?targetDataTable=tv_episode_info&pk_idx='+str(pre_date_and_pk_dict[str(list(tv_epi_info_df.epi_date)[i])])
                # tv_epi_info_admin_url = 'http://skyfall.mycelebs.com:8000/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_info&cd_idx='+str(cd_idx)
                driver.get(edit_url)
                # driver.find_element_by_css_selector(css_selector_date).clear()
                # driver.find_element_by_css_selector(css_selector_date).send_keys(list(tv_epi_info_df.epi_date)[i])
                # driver.find_element_by_css_selector(css_selector_date_str).clear()
                # driver.find_element_by_css_selector(css_selector_date_str).send_keys(list(tv_epi_info_df.epi_num)[i])
                driver.find_element_by_css_selector(css_selector_date_rate).clear()
                driver.find_element_by_css_selector(css_selector_date_rate).send_keys(str(list(tv_epi_info_df.view_rate)[i]))
                btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
                btn.click()
                #
                #
                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(2)

        except:
            print(i, str(list(tv_epi_info_df.epi_date)[i]))
            tv_epi_info_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_info&cd_idx='+str(cd_idx)
            driver.get(tv_epi_info_admin_url)
            css_selector_date = 'body > div.container > div > div > form > div:nth-child(3) > input'
            css_selector_date_str = 'body > div.container > div > div > form > div:nth-child(4) > input'
            css_selector_date_rate = 'body > div.container > div > div > form > div:nth-child(5) > input'


            driver.find_element_by_css_selector(css_selector_date).send_keys(list(tv_epi_info_df.epi_date)[i])
            driver.find_element_by_css_selector(css_selector_date_str).send_keys(list(tv_epi_info_df.epi_num)[i])
            driver.find_element_by_css_selector(css_selector_date_rate).send_keys(str(list(tv_epi_info_df.view_rate)[i]))
             ##### 가짜 데이터 입력
            driver.find_element_by_css_selector(css_selector_naver_search_count).send_keys("0")
            driver.find_element_by_css_selector(css_selector_2049_view_rate).send_keys("0")
            driver.find_element_by_css_selector(css_selector_pay_per_view_rate).send_keys("0")
            #####

            #
            btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
            btn.click()

            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(2)
    else:
        print(list(tv_epi_info_df.cd_idx)[i], str(pd.to_datetime(tv_epi_info_df.epi_date[i])))


driver.close()
    # except:


####################################################################################################################################################

# 2. tv cast 관리 업데이트


xls = pd.ExcelFile( fileName +'_회차별출연진.xlsx')

tv_cast_df = xls.parse('_회차별출연진')
tv_cast_df_for_admin = DataFrame()
tv_cast_df_for_admin['cd_idx'] = tv_cast_df['cd_idx']
tv_cast_df_for_admin['celeb_name'] = tv_cast_df['celeb_name']
tv_cast_df_for_admin['role_detail'] = tv_cast_df['role_detail']
tv_cast_df_for_admin['sub_cd_idx'] = tv_cast_df['sub_cd_idx']
tv_cast_df_for_admin['solr_query'] = tv_cast_df['solr_query']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='/Users/mycelebs/Downloads/chromedriver')
# driver=webdriver.Firefox()
driver.get(f'http://{pid}:{ppw}@dev.mycelebs.com/donut/')
alert = driver.switch_to_alert()
alert.accept()
#adminId
driver.find_element_by_css_selector('#adminId').send_keys('admin')
driver.find_element_by_css_selector('#adminPw').send_keys('admin')
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()




for i in tqdm(range(len(tv_cast_df_for_admin))):
    cd_idx = tv_cast_df_for_admin.cd_idx[i]
    check_url = 'http://dev.mycelebs.com/donut/Celeb/ShowManageTvCeleb?targetDataTable=tv_cast&cd_idx='+str(cd_idx)
    driver.get(check_url)
    r = driver.page_source
    soup = BeautifulSoup(r,'lxml')
    try:
        pre_celeb_key_list =[soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[3].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))]
        time.sleep(0.5)

        tv_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_cast&cd_idx='+str(cd_idx)
        driver.get(tv_cast_admin_url)
        css_selector_query = 'body > div.container > div > div > form > div:nth-child(3) > input'
        css_selector_sub_cd_idx = 'body > div.container > div > div > form > div:nth-child(4) > input'
        css_selector_role = 'body > div.container > div > div > form > div:nth-child(5) > input'
        css_selector_role_detail = 'body > div.container > div > div > form > div:nth-child(6) > input'
        css_selector_role_explain = 'body > div.container > div > div > form > div:nth-child(7) > input'
        css_selector_role_start_date = 'body > div.container > div > div > form > div:nth-child(8) > input'
        css_selector_role_end_date = 'body > div.container > div > div > form > div:nth-child(9) > input'

        celeb_name = list(tv_cast_df_for_admin.celeb_name)[i]
        celeb_key = list(tv_cast_df_for_admin.sub_cd_idx)[i]
        celeb_role_detail = list(tv_cast_df_for_admin.role_detail)[i].strip()
        if celeb_role_detail == '게스트':
            celeb_role = '게스트'
        elif celeb_role_detail == '특별출연':
            celeb_role = '특별출연'
        else:
            celeb_role = '출연'
        celeb_query = list(tv_cast_df_for_admin.solr_query)[i]

        # if    ' 역' in celeb_role_detail:
        #   celeb_query = makeCelebQuery_TV_for_role(celeb_name,celeb_role_detail)
        # else:
        #   celeb_query = makeCelebQuery_TV(celeb_name)

        #time.sleep(random.uniform(0.8,2.0))
        if not str(celeb_key) in pre_celeb_key_list:
            driver.find_element_by_css_selector(css_selector_query).send_keys(celeb_query)
            driver.find_element_by_css_selector(css_selector_sub_cd_idx).send_keys(str(celeb_key))
            driver.find_element_by_css_selector(css_selector_role).send_keys(celeb_role)
            driver.find_element_by_css_selector(css_selector_role_detail).send_keys(celeb_role_detail)
            driver.find_element_by_css_selector(css_selector_role_explain).send_keys(celeb_role_detail)
            driver.find_element_by_css_selector(css_selector_role_start_date).send_keys('2017-01-01')
            driver.find_element_by_css_selector(css_selector_role_end_date).send_keys('2017-12-31')

            btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
            btn.click()

            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(1)
        else:
            pass
    except Exception as e:
        print(e, 'cd_idx: ', cd_idx, ' sub_cd_idx: ', tv_cast_df_for_admin.sub_cd_idx[i])
        pre_celeb_key_list =[soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[3].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))]
        time.sleep(0.5)
        # break
        tv_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_cast&cd_idx='+str(cd_idx)
        driver.get(tv_cast_admin_url)
        css_selector_query = 'body > div.container > div > div > form > div:nth-child(3) > input'
        css_selector_sub_cd_idx = 'body > div.container > div > div > form > div:nth-child(4) > input'
        css_selector_role = 'body > div.container > div > div > form > div:nth-child(5) > input'
        css_selector_role_detail = 'body > div.container > div > div > form > div:nth-child(6) > input'
        css_selector_role_explain = 'body > div.container > div > div > form > div:nth-child(7) > input'
        css_selector_role_start_date = 'body > div.container > div > div > form > div:nth-child(8) > input'
        css_selector_role_end_date = 'body > div.container > div > div > form > div:nth-child(9) > input'

        celeb_name = list(tv_cast_df_for_admin.celeb_name)[i]
        celeb_key = list(tv_cast_df_for_admin.sub_cd_idx)[i]
        celeb_role_detail = list(tv_cast_df_for_admin.role_detail)[i].strip()
        if celeb_role_detail == '게스트':
            celeb_role = '게스트'
        elif celeb_role_detail == '특별출연':
            celeb_role = '특별출연'
        else:
            celeb_role = '출연'
        celeb_query = list(tv_cast_df_for_admin.solr_query)[i]

        # if    ' 역' in celeb_role_detail:
        #   celeb_query = makeCelebQuery_TV_for_role(celeb_name,celeb_role_detail)
        # else:
        #   celeb_query = makeCelebQuery_TV(celeb_name)
        if not str(celeb_key) in pre_celeb_key_list:
            driver.find_element_by_css_selector(css_selector_query).send_keys(celeb_query)
            driver.find_element_by_css_selector(css_selector_sub_cd_idx).send_keys(str(celeb_key))
            driver.find_element_by_css_selector(css_selector_role).send_keys(celeb_role)
            driver.find_element_by_css_selector(css_selector_role_detail).send_keys(celeb_role_detail)
            driver.find_element_by_css_selector(css_selector_role_explain).send_keys(celeb_role_detail)
            driver.find_element_by_css_selector(css_selector_role_start_date).send_keys('2017-01-01')
            driver.find_element_by_css_selector(css_selector_role_end_date).send_keys('2017-12-31')

            btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
            btn.click()

            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(1)
        else:
            pass

driver.close()


####################################################################################################################################################

#no_info에서 에러남

#3

import pandas as pd



fileName = input('회차정보 엑셀 파일명을 입력하세요. YY-MM-DD')

xls = pd.ExcelFile( fileName +'_회차별출연진.xlsx')
tv_epi_cast_df = xls.parse('_회차별출연진')
# pid = 'mycelebsTempUser'
# ppw = 'bx7a8s30FmDH'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='/Users/mycelebs/Downloads/chromedriver')
# driver = webdriver.Chrome(chrome_options = chrome_options)
# driver=webdriver.Firefox()
driver.get(f'http://{pid}:{ppw}@dev.mycelebs.com/donut/')
alert = driver.switch_to_alert()
alert.accept()
#adminId
driver.find_element_by_css_selector('#adminId').send_keys('admin')
driver.find_element_by_css_selector('#adminPw').send_keys('admin')
btn = driver.find_element_by_css_selector('#loginForm > button')
btn.click()
my_cdidx = list(tv_epi_cast_df['cd_idx'])
my_tei_date = list(tv_epi_cast_df['tei_date'])
my_sub_cdidx = list(tv_epi_cast_df['sub_cd_idx'])

for i in tqdm(range(len(tv_epi_cast_df))):
    if pd.to_datetime(time.strftime('%Y-%m-%d')) >= pd.to_datetime(my_tei_date[i]):
        cd_idx = my_cdidx[i]
        check_url = 'http://dev.mycelebs.com/donut/Celeb/ShowManageTvCeleb?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
        driver.get(check_url)
        r = driver.page_source
        soup = BeautifulSoup(r,'lxml')
        try:
            tr_list = soup.find('table').find('tbody').findAll('tr')
            td_list = [[content.findAll('td')[3].text.replace(' 00:00:00',''),content.findAll('td')[2].text] for content in tr_list]
            pre_date_list =[value1 + '_' + value2 for value1, value2 in td_list]
            # time.sleep(0.5)
            td_epi_date = my_tei_date[i]
            check_code = my_tei_date[i] + '_' + str(my_sub_cdidx)[i]

            if not check_code in pre_date_list:
                tv_epi_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
                driver.get(tv_epi_cast_admin_url)
                css_selector_celeb_key = 'body > div.container > div > div > form > div:nth-child(3) > input'
                css_selector_date = 'body > div.container > div > div > form > div:nth-child(4) > input'
                td_epi_date = my_tei_date[i]

                driver.find_element_by_css_selector(css_selector_celeb_key).send_keys(str(my_sub_cdidx[i]))
                driver.find_element_by_css_selector(css_selector_date).send_keys(td_epi_date)


                btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
                btn.click()

                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(0.5)
            else:
                pass

        except:
            tv_epi_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
            driver.get(tv_epi_cast_admin_url)
            css_selector_celeb_key = 'body > div.container > div > div > form > div:nth-child(3) > input'
            css_selector_date = 'body > div.container > div > div > form > div:nth-child(4) > input'
            td_epi_date = my_tei_date[i]

            driver.find_element_by_css_selector(css_selector_celeb_key).send_keys(str(my_sub_cdidx[i]))
            driver.find_element_by_css_selector(css_selector_date).send_keys(td_epi_date)


            btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
            btn.click()

            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(0.5)
        print(i , len(tv_epi_cast_df))

    else:
        print(my_cdidx[i], str(pd.to_datetime(my_tei_date[i])))


driver.close()


# # 3-1
# fileName = input('회차정보 엑셀 파일명을 입력하세요. YY-MM-DD')
#
# xls = pd.ExcelFile( fileName +'_회차별출연진.xlsx')
# tv_epi_cast_df = xls.parse('_회차별출연진')
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='/Users/mycelebs/Downloads/chromedriver')
# # driver=webdriver.Firefox()
# driver.get(f'http://{pid}:{ppw}@dev.mycelebs.com/donut/')
# alert = driver.switch_to_alert()
# alert.accept()
# #adminId
# driver.find_element_by_css_selector('#adminId').send_keys('admin')
# driver.find_element_by_css_selector('#adminPw').send_keys('admin')
# btn = driver.find_element_by_css_selector('#loginForm > button')
# btn.click()
#
# # for i in tqdm(range(0, len(tv_epi_cast_df))):
# for i in tqdm(range(0, len(tv_epi_cast_df))):
#     if pd.to_datetime(time.strftime('%Y-%m-%d')) >= pd.to_datetime(tv_epi_cast_df.tei_date[i]):
#         cd_idx = list(tv_epi_cast_df.cd_idx)[i]
#         check_url = 'http://dev.mycelebs.com/donut/Celeb/ShowManageTvCeleb?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
#         driver.get(check_url)
#         r = driver.page_source
#         soup = BeautifulSoup(r,'lxml')
#         try:
#             pre_date_list =[soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[3].text.replace(' 00:00:00','') +'_'+ soup.find('table').find('tbody').findAll('tr')[i].findAll('td')[2].text for i in range(len(soup.find('table').find('tbody').findAll('tr')))]
#             time.sleep(0.5)
#             td_epi_date = list(tv_epi_cast_df['tei_date'])[i]
#             check_code = list(tv_epi_cast_df['tei_date'])[i] + '_' + str(list(tv_epi_cast_df['sub_cd_idx'])[i])
#
#             if not check_code in pre_date_list:
#                 tv_epi_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
#                 driver.get(tv_epi_cast_admin_url)
#                 css_selector_celeb_key = 'body > div.container > div > div > form > div:nth-child(3) > input'
#                 css_selector_date = 'body > div.container > div > div > form > div:nth-child(4) > input'
#                 td_epi_date = list(tv_epi_cast_df['tei_date'])[i]
#
#                 driver.find_element_by_css_selector(css_selector_celeb_key).send_keys(str(list(tv_epi_cast_df.sub_cd_idx)[i]))
#                 driver.find_element_by_css_selector(css_selector_date).send_keys(td_epi_date)
#
#
#                 btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
#                 btn.click()
#
#                 alert = driver.switch_to_alert()
#                 alert.accept()
#                 time.sleep(1)
#             else:
#                 pass
#
#         except:
#             tv_epi_cast_admin_url = 'http://dev.mycelebs.com/donut/Celeb/ShowTvCelebForm?targetDataTable=tv_episode_cast_relation&cd_idx='+str(cd_idx)
#             driver.get(tv_epi_cast_admin_url)
#             css_selector_celeb_key = 'body > div.container > div > div > form > div:nth-child(3) > input'
#             css_selector_date = 'body > div.container > div > div > form > div:nth-child(4) > input'
#             td_epi_date = list(tv_epi_cast_df['tei_date'])[i]
#
#             driver.find_element_by_css_selector(css_selector_celeb_key).send_keys(str(list(tv_epi_cast_df.sub_cd_idx)[i]))
#             driver.find_element_by_css_selector(css_selector_date).send_keys(td_epi_date)
#
#
#             btn = driver.find_element_by_css_selector('body > div.container > div > div > form > button')
#             btn.click()
#
#             alert = driver.switch_to_alert()
#             alert.accept()
#             time.sleep(1)
#         print(i , len(tv_epi_cast_df))
#
#     else:
#         print(list(tv_epi_cast_df.cd_idx)[i], str(pd.to_datetime(tv_epi_cast_df.tei_date[i])))
#
#
# driver.close()


#############################################################################################

#4 신규회차정보 코드


import os
import pandas as pd
os.chdir('/Users/mycelebs/Desktop/방송')


def check_new_programs_episode(FILE_DATE):
    # 회차정보업데이트 파일
    xls = pd.ExcelFile(FILE_DATE + '_회차정보업데이트.xlsx')
    update_df = xls.parse(xls.sheet_names[1])
    update_df_unique = update_df[['td_daum_id']].drop_duplicates()
    # 회차업데이트_데일리 파일
    new_program = pd.read_excel('회차업데이트_데일리.xlsx')
    new_list = list(new_program['td_daum_id'])
    new_program_list_unique = list(set(new_list))
    # 에피소드 입력 여부 확인
    check_episode = update_df_unique['td_daum_id'].isin(new_program_list_unique)
    episode_in = list(update_df_unique[check_episode]['td_daum_id'])
    episode_not_yet = list(update_df_unique[-check_episode]['td_daum_id'])
    return episode_in, episode_not_yet

episode_in, episode_not_yet = check_new_programs_episode(fileName)

# 새프로그램 중 에피소드가 들어온 것 >> 해당되는 idx는 회차업데이트_데일리.xlsx에서 삭제 + 나(종우)에게 전달(date는 최신회차로 업뎃)
episode_in

#
#episode_not_yet

