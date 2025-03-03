# 递归问题
# 求一个数的阶乘
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num-1) + fibonacci(num - 2)


def  TowerOfHanoi(num):
    if num == 1:
        return 1
    return  2 * TowerOfHanoi(num-1) + 1

print('请输入一个数：\n')
# 获取用户输入，并将其转换为整数
try:
    user_input = int(input())  # input() 函数读取用户输入，默认为字符串，需要转换为整数
    # 调用 factorial 函数并打印结果
    result = factorial(user_input)
    print(f"{user_input} 的阶乘是：{result}\n")
except ValueError:
    # 如果用户输入的不是一个有效的整数，捕获 ValueError 异常并输出错误信息
    print("输入无效，请输入一个整数。\n")

print('请输入一个数：\n')
# 获取用户输入，并将其转换为整数
try:
    user_input = int(input())  # input() 函数读取用户输入，默认为字符串，需要转换为整数
    # 调用 factorial 函数并打印结果
    result = fibonacci(user_input)
    print(f"{user_input} 的斐波那契数列是：{result}\n")
except ValueError:
    # 如果用户输入的不是一个有效的整数，捕获 ValueError 异常并输出错误信息
    print("输入无效，请输入一个整数。\n")


print('请输入一个数：\n')
# 获取用户输入，并将其转换为整数
try:
    user_input = int(input())  # input() 函数读取用户输入，默认为字符串，需要转换为整数
    # 调用 factorial 函数并打印结果
    result = TowerOfHanoi(user_input)
    print(f"{user_input} 级汉诺塔需要移动的次数是是：{result}\n")
except ValueError:
    # 如果用户输入的不是一个有效的整数，捕获 ValueError 异常并输出错误信息
    print("输入无效，请输入一个整数。\n")