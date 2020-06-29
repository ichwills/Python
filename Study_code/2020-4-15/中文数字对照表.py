uppercase_numbers = ("点","零", "壹", "贰", "叁", "肆","伍","陆", "柒", "捌", "玖")
number = input("请输入一个数字：")
if number.isdigit():
    for i in range(len(number)):
        print(uppercase_numbers[int(number[i])], end="")
else:
    print("输入的'",number,"'格式有误,请输入")