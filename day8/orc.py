import pytesseract
from PIL import Image

def shibie(imagepath):
	# 先处理图片，然后再识别
	# 打开图片
	img = Image.open(imagepath)

	# 转化为灰度图片
	img = img.convert('L')

	# img.show()
	# 二值化处理
	threshold = 140
	table = []
	for i in range(256):
	    if i < threshold:
	        table.append(0)
	    else:
	        table.append(1)
	out = img.point(table, '1')

	# out.show()
	img = img.convert('RGB')

	return pytesseract.image_to_string(img)