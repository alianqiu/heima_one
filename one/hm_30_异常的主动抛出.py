
"""

def input_password():

    # 1 提示用户输入密码
    pwd = input("输入密码：")

    # 2 判断密码长度， >=8, 返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3 <8, 主动抛出异常
    print("主动抛出异常")

    #1> 创建异常对象 可使用错误信息字符串作为参数
    ex = Exception("密码长度不够")

    #2> 主动抛出异常
    raise ex

print(input_password())


"""
"""
输入密码：a
主动抛出异常
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/heima/test/hm_30_异常的主动抛出.py", line 23, in <module>
    print(input_password())
  File "/Users/user/PycharmProjects/heima/test/hm_30_异常的主动抛出.py", line 21, in input_password
    raise ex
Exception: 密码长度不够
"""
def input_password():

    # 1 提示用户输入密码
    pwd = input("输入密码：")

    # 2 判断密码长度， >=8, 返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3 <8, 主动抛出异常
    print("主动抛出异常")

    #1> 创建异常对象
    ex = Exception("密码长度不够")

    #2> 主动抛出异常
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)
"""
输入密码：a
主动抛出异常
密码长度不够
"""