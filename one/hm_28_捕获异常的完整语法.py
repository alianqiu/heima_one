
"""
try:
    # 尝试执行的代码
    pass
except 错误类型1:
    # 针对错误类型1 对应的代码处理
    pass
except 错误类型2:
    # 针对错误类型2 对应的代码处理
except (错误类型3,错误类型4):
    # 针对错误类型3和4 对应的代码处理
except Exception as result:
    # 打印错误信息
    print(result)
else:
    # 没有异常才会执行的代码
finally:
    #无论有无异常，都会执行的代码
    print("无论有无异常，都会执行的代码")
"""


"""

"""
try:

    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用8除以用户输入的整数并且输出
    result = 8 / num

    print(result)


except ValueError:
    print("请输入正确的整数")

except Exception as result:
    print("未知错误： %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否出现错误，都会执行的代码")
print("-" * 50)
"""
输入一个整数：1
8.0
尝试成功
无论是否出现错误，都会执行的代码
--------------------------------------------------
"""
"""
输入一个整数：0
未知错误： division by zero
无论是否出现错误，都会执行的代码
--------------------------------------------------
"""
