import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
from PIL import Image
from tqdm import tqdm
import urllib.request
import os
import shutil
import re

def read_excel():
	df = pd.DataFrame()
    db_connection = # 데이터베이스 정보
	info = pd.read_sql('SELECT * FROM yelp_no_img',con=db_connection)
    df = pd.read_excel('/Users/mycelebs/yelp_info.xlsx') #yelp_info가 원본
    business_id = df[['cd_idx', 'yd_business_id']]
    #business_id = list(df['yd_business_id']) 
    return business_id #총 43287개 > 0~43286
	#info.to_excel('yelp_info.xlsx',index=False)

# a = read_excel()
# b['cd_idx_0'] = b['cd_idx'].apply(lambda x: str(x)+'_0')
# #a['cd_idx'].apply(lambda x: str(x)+'_0')
# a['cd_idx_0'] = a['cd_idx'].apply(lambda x: str(x)+'_0')
# a['cd_idx_0'][0]
# a['cd_idx'][0]
# a['yd_business_id']

def read_excel_all():
    df = pd.DataFrame()
    db_connection = # 데이터베이스 정보
    info = pd.read_sql('SELECT * FROM yelp_no_img',con=db_connection)
    df = pd.read_excel('/Users/mycelebs/yelp_info.xlsx') #yelp_info가 원본
    return df #총 43287개 > 0~43286
    #info.to_excel('yelp_info.xlsx',index=False)

def get_url(b_id): #read_excel()[0~len]
    r = requests.Session()
    try:
        r.headers.update({
            'tab':'food',
            'referer':f'https://www.yelp.com/biz_photos/{b_id}'
            })
        req = r.get(f'https://www.yelp.com/biz_photos/{b_id}')
        bs = BeautifulSoup(req.text, 'lxml')
        imgs = bs.select('li div.photo-box.photo-box--interactive img')
        origin_urls = [i['src'] for i in imgs][:2]
        for i in range(len(origin_urls)):
            origin_urls[i] = origin_urls[i].replace("258s","o")
    except:
        pass
    return origin_urls


# def gather_code_data():
#     total_count = len(read_excel())
#     code_arr = []
#     for i in range(total_count):
#         code_arr.append(get_url(read_excel()[i]))
#         #print(code_arr[i])
#     return code_arr


def save_image_url(code_arr): #인수 : gather_code_data()
    new_path_1 = '/Users/mycelebs/Desktop/_0/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/'
    for i in tqdm(range(len(code_arr))): #7
        for j in range(len(code_arr[i])): #2
            try:
                code_arr[i][j] = code_arr[i][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i][j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                if str(j) == '0':
                    crop_img.save(new_path_1+ str(business_id[i])+"_"+str(j)+".jpg")
                else:
                    crop_img.save(new_path_2+ str(business_id[i])+"_"+str(j)+".jpg")
                    
                #save_path = '/Users/mycelebs/yelp_image/'
                #urllib.request.urlretrieve(str(image_url[i][j]),save_path+str(read_excel()[i])+"_"+str(j)+".jpg")
                print(str(read_excel()[i])+"_"+str(j)+".jpg")
            except Exception as e:
                print(e)
                pass

def save_image_url2(code_arr): #마지막 40000~43287 > 40000폴더로 옮기기(수동)
	new_path_1 = '/Users/mycelebs/Desktop/_0/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/'
    for i in tqdm(range(40000,43287)): #7
        for j in range(0,1): #2
            try:
                code_arr[i-40000][j] = code_arr[i-40000][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i-40000][j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                crop_img.save(new_path_1+ a['cd_idx_0'][i]+".jpg") #a['cd_idx_0'][0]
                # if str(j) == '0':
                #     crop_img.save(new_path_1+ str(business_id[i])+"_"+str(j)+".jpg")
                # else:
                #     crop_img.save(new_path_2+ str(business_id[i])+"_"+str(j)+".jpg")
                    
                #save_path = '/Users/mycelebs/yelp_image/'
                #urllib.request.urlretrieve(str(image_url[i][j]),save_path+str(read_excel()[i])+"_"+str(j)+".jpg")
                print(str(read_excel()[i])+"_"+str(j)+".jpg")
            except:
                pass

def save_image_url3(code_arr): #30000~40000
	new_path_1 = '/Users/mycelebs/Desktop/_0/40000/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/40000/'
    for i in tqdm(range(30000,40000)): #7
        for j in range(0,2): #2
            try:
                code_arr[i-30000][j] = code_arr[i-30000][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i-30000][j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                crop_img.save(new_path_1+ a['cd_idx_0'][i]+".jpg")
                # if str(j) == '0':
                #     crop_img.save(new_path_1+ str(business_id[i])+"_"+str(j)+".jpg")
                # else:
                #     crop_img.save(new_path_2+ str(business_id[i])+"_"+str(j)+".jpg")
                    
                #save_path = '/Users/mycelebs/yelp_image/'
                #urllib.request.urlretrieve(str(image_url[i][j]),save_path+str(read_excel()[i])+"_"+str(j)+".jpg")
                print(str(read_excel()[i])+"_"+str(j)+".jpg")
            except:
                pass

def save_image_url4(code_arr): #20000~30000
	new_path_1 = '/Users/mycelebs/Desktop/_0/30000/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/30000/'
    for i in tqdm(range(20000,30000)): #7
        for j in range(0,2): #2
            try:
                code_arr[i-20000][j] = code_arr[i-20000][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i-20000][j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                crop_img.save(new_path_1+ a['cd_idx_0'][i]+".jpg")
                # if str(j) == '0':
                #     crop_img.save(new_path_1+ str(business_id[i])+"_"+str(j)+".jpg")
                # else:
                #     crop_img.save(new_path_2+ str(business_id[i])+"_"+str(j)+".jpg")
                    
                #save_path = '/Users/mycelebs/yelp_image/'
                #urllib.request.urlretrieve(str(image_url[i][j]),save_path+str(read_excel()[i])+"_"+str(j)+".jpg")
                print(str(read_excel()[i])+"_"+str(j)+".jpg")
            except:
                pass

def save_image_url5(code_arr): #10000~20000
	new_path_1 = '/Users/mycelebs/Desktop/_0/20000/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/20000/'
    for i in tqdm(range(10000,20000)): #7
        for j in range(0,2): #2
            try:
                code_arr[i-10000][j] = code_arr[i-10000][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i-10000][j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                crop_img.save(new_path_1+ a['cd_idx_0'][i]+".jpg")
                # if str(j) == '0':
                #     crop_img.save(new_path_1+ str(business_id[i])+"_"+str(j)+".jpg")
                # else:
                #     crop_img.save(new_path_2+ str(business_id[i])+"_"+str(j)+".jpg")
                    
                #save_path = '/Users/mycelebs/yelp_image/'
                #urllib.request.urlretrieve(str(image_url[i][j]),save_path+str(read_excel()[i])+"_"+str(j)+".jpg")
                print(str(read_excel()[i])+"_"+str(j)+".jpg")
            except:
                pass

def save_image_url6(code_arr): #0~10000
	new_path_1 = '/Users/mycelebs/Desktop/_0/10000/' #_0 or _1    
    new_path_2 = '/Users/mycelebs/Desktop/_1/10000/'
    for i in tqdm(range(0,10000)): #7
        for j in range(0,2): #2
            try:
                code_arr[i][j] = code_arr[i][j].replace("https","http")
                img = Image.open(requests.get(str(code_arr[i][ j]), stream=True).raw)
                crop_img = img.resize((400, 400), Image.ANTIALIAS)
                crop_img.save(new_path_1+ a['cd_idx_0'][i]+".jpg")
            except:
                pass

def gather_code_data_2(business_id):
    total_count = len(business_id)
    code_arr = []
    for i in tqdm(range(total_count)):
        code_arr.append(get_url(business_id.get(i)))
    return code_arr

def gather_code_data_3(business_id):
    total_count = len(business_id)
    code_arr = []
    for i in tqdm(range(10000,20000)):
        code_arr.append(get_url(business_id.get(i)))
    return code_arr

def gather_code_data_4(business_id):
    total_count = len(business_id)
    code_arr = []
    for i in tqdm(range(20000,30000)):
        code_arr.append(get_url(business_id.get(i)))
    return code_arr

def gather_code_data_5(business_id):
    total_count = len(business_id)
    code_arr = []
    for i in tqdm(range(30000,40000)):
        code_arr.append(get_url(business_id.get(i)))
    return code_arr

def gather_code_data_6(business_id):
    total_count = len(business_id)
    code_arr = []
    for i in tqdm(range(40000,43287)):
        code_arr.append(get_url(business_id[i]))
    return code_arr




###########################
#2018.09.14 돌린 것 
a = read_excel() #a : cd_idx,business_id,cd_idx_0
code_arr1 = gather_code_data_2(a['yd_business_id'][:10000]) #터미널1 gater_2
code_arr2 = gather_code_data_3(a['yd_business_id'][10000:20000]) #터미널2 gater_3
code_arr3 = gather_code_data_4(a['yd_business_id'][:30000]) #터미널3 gater_4
code_arr4 = gather_code_data_5(a['yd_business_id'][30000:40000]) #터미널200004 gater_5 
code_arr5 = gather_code_data_6(a['yd_business_id'][40000:]) #터미널5 gater_6 

save_image_url2(code_arr5) #40000~43287 이미지 저장 #지금 하는중 > 끝
save_image_url6(code_arr1) #0~10000 이미지 저장 #지금 하는중(10000 폴더) >
save_image_url5(code_arr2) #10000~20000 이미지 저장 #지금 하는중(20000 폴더) > 
save_image_url4(code_arr3) #20000~30000 이미지 저장 #지금 하는중(30000 폴더) >
save_image_url3(code_arr4) #30000~40000 이미지 저장 #지금 하는 중(40000 폴더) >

############################################################





##########################################################
a['yd_business_id'][10000]
b['yd_business_id'][10000]
code_arr2 = gather_code_data_3(b['yd_business_id'][10000:20000])
###################

df = pd.read_excel('/Users/mycelebs/yelp_info_test.xlsx')
business_id = list(df['yd_business_id'])
a = read_excel()
len(business_id)

###############################
result = gather_code_data_2(business_id)
save_image_url


save_image_url(result) #이거 돌리면 됨!
###################
result1 = gather_code_data_2(business_id[:10000]) #터미널1
result2 = gather_code_data_2(business_id[10000:20000]) #터미널2
result3 = gather_code_data_2(business_id[20000:30000]) #터미널3
result4 = gather_code_data_2(business_id[30000:40000]) #터미널4
result5 = gather_code_data_2(business_id[40000:]) #터미널5 40000~43287


save_image_url6(result1) #0~10000사진들 저장
save_image_url5(result2) #10000~20000사진들 저장
save_image_url4(result3) #20000~30000사진들 저장
save_image_url3(result4) #30000~40000사진들 저장
save_image_url2(result5) #result5[40000-40000][0]로 저장(마지막터미널에서 돌리는중)

len(result5)
business_id[43286]

len(result5[3286])

for i in range(40000,40010):
	for j in range(0,2):
		print(i)
		print(j)



len(a[0])


business_id[0]
len(business_id)

gather_code_data_2(business_id)

gather_code_data()
save_image_url(gather_code_data())
code_arr

a =[gather_code_data()[x:x+3] for x in range(0, len(gather_code_data()), 3)]




