name=(input("姓名："))
studentID=(input("学号："))
height=float(input("请输入身高(米)："))
weight=float(input("请输入体重(公斤)："))
BMI=float(float(weight)/(float(height)**2))
print("结果：")
print("    身高    :{:.2f}米".format(height))
print("    体重    :{:.2f}公斤".format(weight))
print("    BMI     :{:.2f}".format(BMI))