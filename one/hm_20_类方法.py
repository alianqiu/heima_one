
"""
@classmethod
def 类方法名(cls):
  pass

类方法需要用 修饰器 @classmethod 来标识 告诉解释器这是一个类方法
类方法第一个参数 cls
 由哪个类 调用的方法，方法内的cls 就是 哪个类的引用
 这个参数和实例方法 的第一个参数 self 类似
 提示：使用其他名称也可以，不过习惯使用cls
通过 类名， 调用 类方法，调用方法时， 不需要传递cls参数
在方法内部
  可以通过 cls. 访问类的属性
   也可以通过 cls. 访问其他的类方法
"""
class Tool:

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值 + 1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count() #工具对象的数量 2