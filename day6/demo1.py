# 通过用户输入数字，计算阶乘。
num = int(input("请输入一个您想要的数字"))
def jie(n):
    if n == 1:
        return 1
    elif n > 1:
        n *= jie(n-1)
        return n
print("该数字的阶乘是",jie(num))
