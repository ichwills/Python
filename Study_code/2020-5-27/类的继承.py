class Animals102:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")
class Dog102(Animals102):
    def bark(self):
        print("吠")
class XiaoTianQuan102(Dog102):
    def fly(self):
        print("飞")
class Cat102(Animals102):
    def catch(self):
        print("抓")
dw=Animals102()
g=Dog102()
xtq=XiaoTianQuan102()
m=Cat102()
dw.sleep()
g.bark()
m.catch()
xtq.fly()

