from PIL import Image, ImageDraw, ImageFont


img = Image.open("E:\code\python\StudyCode\code\hy.jpg")

# 调整尺寸
def Resize():
    new_img = img.resize((480,480))
    new_img = new_img.convert("RGB")
    new_img.save('E:\code\python\StudyCode\code\hy2.jpg')


#添加文字
def Add_text():
	font = ImageFont.truetype('simsun.ttc',24)
	img = Image.open("E:\code\python\StudyCode\code\hy2.jpg")
	draw = ImageDraw.Draw(img)
	draw.text((0,60),'程越\n18010102\nhelloworld',(0,0,0),font=font)
	img.save('E:\code\python\StudyCode\code\hy2.jpg')

#测试
# img2 = Image.open("E:\code\python\StudyCode\code\hy2.jpg")
# print("原图像的大小:",img.size)
# print("新图像的大小:",img2.size) 
# img2.pause(1)

Resize()
Add_text()