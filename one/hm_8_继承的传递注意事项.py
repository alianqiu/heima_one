

class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")



class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

class Cat(Animal):

    def catch(self):
        print("抓老鼠")

# 创建啸天犬对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.eat()

# 不符合继承传递性 所以不能调用
# xtq.catch()