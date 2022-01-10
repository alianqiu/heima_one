
"""
注意
开发时 应该尽量避免不同父类中存在同名的方法
如果父类之间 存在 同名的属性或者方法 应尽量避免 使用多继承

Python 中的 MRO - 方法搜索顺序
python 中 针对 类 提供了一个 内置属性 __mro__ 可以查看 方法 搜索顺序
MRO 是 method resolution order, 主要用于 在多继承时判断 方法 属性 的调用路径
"""
class A:

    def test(self):
        print("A -- test 方法")

    def demo(self):
        print("A -- demo 方法")


class B:

    def test(self):
        print("B -- test 方法")

    def demo(self):
        print("B -- demo 方法")

class C(A, B):
    """多继承可以让子类对象 同时具有多个父类的属性和方法"""
    pass

# 创建子类对象

c = C()

c.test()
c.demo()
"""
A -- test 方法
A -- demo 方法
"""

"""
如果先继承B 再继承A 即 C(B, A)
则运行结果
B -- test 方法
B -- demo 方法
"""

# 确定C类对象调用方法的顺序

print(C.__mro__)
"""
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
"""

