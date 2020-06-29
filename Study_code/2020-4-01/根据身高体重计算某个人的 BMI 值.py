height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height * height)
print("    身高    : {:.2f}米".format(height))
print("    体重    : {:.2f}公斤".format(weight))
print("    BMI     : {:.2f}".format(BMI))
if BMI < 18.5:
    print('    状态   ',':','过轻')
elif 18.5 <= BMI <= 23.9:
    print('    状态   ',':','正常')
elif 24 <= BMI <= 27:
    print('    状态   ',':','过重')
elif 28 <= BMI <= 32:
    print('    状态   ',':','肥胖')
else:
    print('    状态   ',':','非常肥胖')