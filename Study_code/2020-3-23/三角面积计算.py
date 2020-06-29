name=(input("姓名："))
studentID=(input("学号："))
print("请依次输入三个整数作为三角形的三条边长,以回车分隔：\n")
one_len = int(input())
two_len = int(input())
three_len = int(input())
c = (one_len + two_len + three_len) / 2
s = (c * (c - one_len) * (c - two_len) * (c - three_len)) ** 0.5
print('三角形(',one_len,two_len,three_len,')面积为%0.1f' % s)
