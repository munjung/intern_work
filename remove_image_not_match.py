import os
import pandas as pd


trevari_excel = pd.read_excel('/Users/mycelebs/Desktop/trevari_cd_idx.xlsx', dtype=str)
trevari_excel.columns
cd_idx = trevari_excel['cd_idx']
trd_ISBN = trevari_excel['trd_ISBN']

# list(trd_ISBN)


path = '/Users/mycelebs/Desktop/trevari_background_image_ISBN'
isbn_list = os.listdir(path)


#type(isbn_list[0][:-4] )
for i in range(len(isbn_list)):
	if isbn_list[i][:-4] not in list(trd_ISBN):
		os.remove(path+'/'+isbn_list[i])
