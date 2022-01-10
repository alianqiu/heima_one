
"""
异常的传递-- 当 函数/方法 执行 出现异常， 会将异常传递 给 函数/方法 的
调用一方
如果 传递到主程序， 仍然 没有异常处理，程序才会被终止
"""
"""
def demo1():
    return int(input("输入整数："))

print(demo1())
"""

"""
输入整数：a
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/heima/test/hm_29_异常的传递.py", line 11, in <module>
    print(demo1())
  File "/Users/user/PycharmProjects/heima/test/hm_29_异常的传递.py", line 9, in demo1
    return int(input("输入整数："))
ValueError: invalid literal for int() with base 10: 'a'
"""

"""
def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

print(demo2())
"""

"""
输入整数：a
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/heima/test/hm_29_异常的传递.py", line 29, in <module>
    print(demo2())
  File "/Users/user/PycharmProjects/heima/test/hm_29_异常的传递.py", line 27, in demo2
    return demo1()
  File "/Users/user/PycharmProjects/heima/test/hm_29_异常的传递.py", line 24, in demo1
    return int(input("输入整数："))
ValueError: invalid literal for int() with base 10: 'a'
"""
def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())

except Exception as result:
    print("未知错误 %s " % result)

"""
输入整数：a
未知错误 invalid literal for int() with base 10: 'a' 
"""
