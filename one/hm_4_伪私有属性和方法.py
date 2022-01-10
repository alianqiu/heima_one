

class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        #在对象的方法内部，是可以访问对象的私有属性的
        print ("%s 的年龄是： %d" % (self.name, self.__age))

xiaofang = Women("小芳")

# 伪私有属性在外界能被直接访问
print (xiaofang._Women__age)

# 伪私有属性在外界能被直接访问
xiaofang._Women__secret()


