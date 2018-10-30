import pandas as pd
import pymysql
import requests
import time
from tqdm import tqdm
import urllib.request

file_path = '/Users/mycelebs/Desktop/18-09-12_회차별출연진.xlsx' 

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




