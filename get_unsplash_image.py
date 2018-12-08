import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import os
from tqdm import tqdm

path = '/Users/mycelebs/Desktop/부킹/'
city_df = pd.read_excel('/Users/mycelebs/Desktop/문정.xlsx')

os.mkdir(path)
failed_dict = []

type(str(city_df['cd_idx'][0]))
os.chdir(path)
url = 'https://unsplash.com/search/photos/london'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
imsi = soup.findAll('img', itemprop='thumbnailUrl')
ims = imsi[0]['srcset'].split('w, ')
for _, row in tqdm(city_df.iterrows()):
    cnt = 0
    url = 'https://unsplash.com/search/photos/' + row['cd_name']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    os.mkdir(path + row['cd_name'])
    os.chdir(path + row['cd_name'])
    image_url = soup.findAll('img', itemprop='thumbnailUrl')
    print(len(image_url))
    try:
        for i in range(20):
            img = image_url[i]
            img = img['srcset'].split('w, ')
            img_len = len(img)
            down_img = img[img_len - 1]
            down_img = down_img[:down_img.find(' ')]
            print(down_img)
            urllib.request.urlretrieve(down_img, str(row['cd_idx']) + '_' + str(i+1) + '.jpg')
    except:
        failed = {'cd_idx' : row['cd_idx'], 'cd_name' : row['cd_name']}
        failed_dict.append(failed)
        continue

os.chdir(path)
failed = pd.DataFrame(failed_dict)
failed.to_excel('falied_list.xlsx')

