# 列表numbers中存储了一组数，numbers = [ 1, 5, -12, 37, 6,93, 100 ]
# ，将这组数按照奇数偶数分别存储到两个列表even和odd中。
def jiou(list):
    even = []
    odd = []
    for i in list:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    print("偶数列表是",odd)
    print("奇数列表是",even)
import random
l = []
for i in range(10):
    num = random.randrange(1,100)
    l.append(num)
jiou(l)

# 编写一个四则混合运算的程序，对输入的数据做好异常处理。（40分）
num1 = input("请输入一个数")
num2 = input("请输入另一个数")
str = input("请输入想要进行的运算符")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 * num2)
    def hun(n1,n2,yun):
        if yun == '+':
            print("两者之和是",n1+n2)
        elif yun == '-':
            print("两者之差是",n1-n2)
        elif yun == '*':
            print("两者之积是",n1*n2)
        elif yun == '/':
            print("两者之商是",n1/n2)
    hun(num1,num2,str)
except:
    print("请输入数字")



