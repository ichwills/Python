raw_data = (input('请输入数字密码：'))
if raw_data.isdigit():
    num_asc = 0
    str_pwd = ''
    for i in raw_data:
        ascii_val = ord(i)
        num_asc = ascii_val + num_asc
        str_pwd += str(ascii_val)
        reversal_num = str_pwd[::-1]
        encryption_num = int(reversal_num) + num_asc
    print(f"加密后的密码为：{encryption_num}")
else:
    print("输入的密码格式有误")