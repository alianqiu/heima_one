
"""
使用类名 创建对象时， Python 的解释器 首先 会 调用 __new__方法为对象
分配空间

__new__ 是一个由 object 基类提供的 内置的静态方法， 主要作用有两个：
 1 在内存中为对象 分配空间
 2 返回 对象的引用


Python 的解释器获得对象的 引用 后， 将引用作为 第一个参数， 传递给 __init__

"""
class MusicPlayer:

    def __new__(cls, *args, **kwargs):
        # 1 创建对象时， new方法会被自动调用
        print("创建对象，分配空间")

        # 2 为对象分配空间
        instance = super().__new__(cls)

        # 3 返回对象的引用
        return instance


    def __init__(self):
        print("播放器初始化")

# 创建播放器对象
player = MusicPlayer()

print(player)