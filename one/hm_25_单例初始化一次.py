
"""
在每次使用 类名() 创建对象时， Python的解释器都会自动调用两个方法：
  __new__分配空间
  __init__对象初始化

23小节中 对__new__方法改造后 每次都会得到 第一次被创建对象的引用
但是 初始化方法还会被再次调用

需求：
 让 初始化动作 只被 执行一次

解决方法
1 定义一个类属性 init_flag 标记是否 执行过初始化动作，初始值 False
2 在__init__方法中，判断 init_flag, 如果为False 就执行初始化动作
3 然后将 init_flag， 设置为 True
4 这样 再次 自动 调用 __init__方法时， 初始化动作就不会被再次执行了
"""
class MusicPlayer:

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1 判断类属性是否是空对象
        if cls.instance is None:
            # 2 调用父类的方法， 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 2 如果没有执行过，再执行初始化动作
        print("初始化播放器")

        # 3 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
'''
初始化播放器
<__main__.MusicPlayer object at 0x10f2735b0>
<__main__.MusicPlayer object at 0x10f2735b0>
'''


