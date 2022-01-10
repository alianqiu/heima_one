
"""
子类对象 不能在自己的方法内部 直接访问父类的 私有属性 或 私有方法
子类对象 可以通过父类的 公有方法 间接 访问到 私有属性 或 私有方法

私有属性 私有方法 是对象的隐私， 不对外公开， 外界 以及 子类 都不能直接访问
私有属性 私有方法 通常用于做一些内部的事情
"""
class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法 %d" % self.__num2)

        self.__test()

class B(A):

    def demo(self):

        # 1 访问父类的私有属性 不行的 编译报错
        print ("访问父类的私有属性 %d" % self.__num2)

        # 2 访问父类的私有方法 不行的 编译报错
        self.__test()

        # 3 访问父类的公有属性
        print("子类方法 %d" % self.num1)

        # 4 调用父类的公有方法
        self.test()



# 创建一个子类对象
b = B()

print(b)

#在外界访问对象的公有属性/调用公有方法
print(b.num1)
print(b.test() )