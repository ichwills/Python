def oper(parm_one, parm_two):
    operator = input('请选择要执行的运算符：[+,-,*,/]' + '\n')
    if operator == "+":
        print("计算结果为:", +parm_one + parm_two)
    elif operator == '-':
        print("计算结果为:", parm_one - parm_two)
    elif operator == '*':
        print("计算结果为:", parm_one * parm_two)
    elif operator == '/':
        if parm_two == 0:
            print('被除数不能为 0')
        else:
            print("计算结果为:", parm_one / parm_two)
    else:
        print("选择的运算符有错")
num_one = int(input('请输入第一个数:'))
num_two = int(input('请输入第二个数:'))
oper(num_one, num_two)