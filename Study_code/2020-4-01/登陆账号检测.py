count = 0
while count < 3:
    user = input("请输入您的账号：")
    pwd = input("请输入您的密码：")
    if user == 'admin' and pwd == '123':
        print('登录成功')
        break
    else:
        print("用户名或密码错误")
        count += 1
    if count == 3:
        print("输入错误次数过多，请稍后再试")
    else:
        print(f"您还有{3-count}次机会")