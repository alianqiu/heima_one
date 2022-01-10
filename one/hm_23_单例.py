
"""
设计模式
  设计模式 是 前任工作的总结和提炼， 通常，被人们广泛流传的设计模式都是针对
某一特定问题 的成熟的解决方案
  使用 设计模式 是为了可重用代码，让代码更容易被他人理解 保证代码可靠性

单例设计模式
  目的 -- 让类 创建的对象，在系统中 只有 唯一的一个实例
  每一次执行 类名() 返回的对象， 内存地址是相同的

音乐播放 对象
回收站 对象
打印机 对象
"""
class MusicPlayer:

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1 判断类属性是否是空对象
        if cls.instance is None:
            # 2 调用父类的方法， 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3 返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
'''
<__main__.MusicPlayer object at 0x10f2735b0>
<__main__.MusicPlayer object at 0x10f2735b0>
'''


