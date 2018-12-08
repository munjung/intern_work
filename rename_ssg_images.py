import os
import pandas as pd
from tqdm import tqdm
import glob
import numpy
import math

#엑셀 경로
origin_excel = pd.read_excel('/Users/mycelebs/Desktop/ssg_excel.xlsx', dtype=str)
origin_cd_idx = origin_excel['cd_idx']
origin_ssg_code = origin_excel['ssgdfm_code']

#이미지 경로
path = r'/Users/mycelebs/Desktop/img'
img_code_list = os.listdir(path)
img_code_list.sort() 

#이미지들의 파일명
img_code_arr = []
for i in range(len(img_code_list)):
	codes = img_code_list[i].split('.jpg')
	img_code_arr.append(codes)

img_code_df = []
for i in range(len(img_code_arr)):
	names = img_code_arr[i][0]
	img_code_df.append(names)

img_name_df = pd.DataFrame({'ssgdfm_code':img_code_df})
img_name_df.to_excel('/Users/mycelebs/Desktop/img_ssg.xlsx')

compare_excel = pd.read_excel('/Users/mycelebs/Desktop/img_ssg.xlsx')
print(compare_excel.columns)

#ssgdm_code 매칭 
merge_result = pd.merge(origin_excel[['cd_idx','ssgdfm_code']], compare_excel[['ssgdfm_code']], how='left')

#code 매칭이 안되는 것들이 있음
for index, oldname in enumerate(img_code_list):
	if math.isnan(float(merge_result['cd_idx'][index])):
		pass
	else:
		os.rename(path+'/'+oldname, path+'/'+str(merge_result['cd_idx'][index])+'_0.jpg')



# for index, oldfile in enumerate(glob.glob("*.jpg"), start=0):
# 	print(oldfile)
