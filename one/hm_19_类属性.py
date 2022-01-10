
"""
Python中一切皆对象
class AAA: 定义的类属于 类对象
obj1 = AAA() 属于实例对象

程序运行时， 类 同样 会被加载到内存
在Python中， 类 是一个特殊的对象 -- 类对象

程序运行时 类对象 在内存中 只有一份 ，使用一个类 可以创建出 很多对象实例
除了封装 实例的 属性和方法外，类对象 还可以拥有自己的 属性和方法
"""
class Tool:

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值 + 1
        Tool.count += 1

# 1 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2 输出工具 对象的总数
print(Tool.count) # 3 推荐
print(tool3.count) # 3 （不推荐 ） 实例对象找不到这个属性 就会往上 找到类对象属性