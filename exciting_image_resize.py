from PIL import Image

title = input('영화제목 >')
img_file_path = '/Users/mycelebs/Desktop/익사이팅엘_사진수정/'+'영화_'+str(title)+'.jpg'
img = Image.open(open(img_file_path, 'r+b'))
img_admin = img.resize((int(640*img.width / img.height), 640))
img_w, img_h = img_admin.size

background = Image.new('RGB', (640, 640), (255, 255, 255, 255))
bg_w, bg_h = background.size
offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
background.paste(img_admin, offset) 
background.save('/Users/mycelebs/Desktop/익사이팅엘_사진수정/수정_320/'+'영화_'+str(title)+'_320.jpg') 
img_color = img.resize((int(640 * img.width / img.height), 640))
img_color.save('/Users/mycelebs/Desktop/익사이팅엘_사진수정/수정_640/'+'영화_'+str(title)+'_640.jpg') 
