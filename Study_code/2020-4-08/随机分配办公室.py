import random
# 定义一个列表用来保存 3 个办公室
offices = [[], [], []]
# 定义一个列表用来存储 8 位老师的名字
names = ['张老师', '李老师', '赵老师', '高老师','刘老师', '周老师', '王老师', '吴老师']
for name in names:
    # 将 8 位老师按照索引为 0、1、2 进行分组
    index = random.randint(0, 2)
    # print(index)
    # 将 8 位老师放在不同列表中
    offices[index].append(name)
    flag = 1
for tempNames in offices:
    print('办公室%d 安排了 %d 位老师,他们是:\n' % (flag, len(tempNames)))
    flag += 1
    for name in tempNames:
        print("%s" % name, end=' ')
        print(" ")