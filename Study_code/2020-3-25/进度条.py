import time 
studentID=(input("学号："))
studentID_list=list(map(int,list(studentID)))
num=studentID_list[-1]
print("\n","="*40,"开始下载","="*40)
data=100
def progress_bar():
    for i in range(0, data+1,num):
        a="#"*i
        b="."*(data-i-4)
        c=(i/data)*100
        print("\r{:.0f}%[{}{}]".format(c,a,b),end="")
        time.sleep(0.5)
        print("\r100%[{}]".format(a),end="")
progress_bar()
print("\n","="*40,"下载完成","="*50)