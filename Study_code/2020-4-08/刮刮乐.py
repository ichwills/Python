reward_info = ["谢谢惠顾", "一等奖", "三等奖", "谢谢惠顾", "谢谢惠顾","三等奖", "二等奖", "谢谢惠顾"]
num = int(input("请输入刮去的位置(1~8)："))
if 0 <= num <= len(reward_info):
    info = reward_info[num - 1]
    print("第",num,"块兑奖区的结果是",f"{info}")
else:
    print("该编号有误!")