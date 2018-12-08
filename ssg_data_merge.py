import pandas as pd
import pymysql

default_path = '/Users/mycelebs/Desktop/jjongwoo/'

def get_database(table_name):
  host, database, user, passwd = '' 
	db_connection = pymysql.connect(host= host, database= database, user= user, passwd= passwd, charset='utf8')
	db_info = pd.read_sql('SELECT ssgdfm_code,ssgdfm_color,ssgdfm_star,ssgdfm_size,ssgdfm_rgb FROM' +table_name+"'", con=db_connection)  # idx있는 것들만
	return db_info

def to_excel(db_info, path):
	db_info.to_excel(path, index = False)

def read_excel(path):
	excel_result = pd.read_excel(path, dtype=str)
	return excel_result





txt_file = pd.read_json(default_path+'재원님_전달받은_ssg한글문서내용.txt')
txt_file.to_excel('ssg.xlsx')

txt_file_excel = pd.read_excel('ssg.xlsx', dtype = str)
ssg_eye_data = pd.read_excel(default_path+'ssgdfm_eye.xlsx', dtype=str)

ssg_lip_data = pd.read_excel(default_path+'ssgdfm_lip.xlsx', dtype=str)


ssg_eye_data.columns
ssg_lip_data.columns

ssg_eye_data['ssgdfm_code']
ssg_lip_data['ssgdfm_code']
#ssgdfm_color,ssgdfm_star,ssgdfm_size,ssgdfm_rgb
result1 = pd.merge(txt_file_excel[['ssgdfm_code']],ssg_eye_data[['ssgdfm_code','ssgdfm_color','ssgdfm_star','ssgdfm_size','ssgdfm_rgb']], how='left')

result1 = pd.merge(txt_file_excel, ssg_eye_data, on = 'ssgdfm_code',how='left')
result1.to_excel(default_path+'result1.xlsx', index = False)

result2 = pd.merge(txt_file_excel, ssg_lip_data, on = 'ssgdfm_code',how='left')
result2.to_excel(default_path+'result2.xlsx', index = False)


