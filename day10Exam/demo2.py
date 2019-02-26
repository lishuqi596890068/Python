# 2.随机生成一个字符串，长度为20，输入一个正整数num，0<num<20，
# 将字符串前num位顺次置于字符串最后，使字符串第num+1位变为新字符串的第一位，
# 其后顺次作为第2、3。。位。对输入的num做好异常处理。（40分）
import random
strlist = ('ABCDEFG')
str = ''
for i in range(20):
    str += random.choice(strlist)+''
print(str)
num = input("请输入一个正整数")
try:
    num = int(num)
    if num >=20 or num <=0:
        print("输入的数值需要在0到二十之间")
    else:
        str1 = str[:num+1]
        print(str1)
        str2 = str[num+1:]
        print(str2)
        str = str2 + str1
        print(str)
except:
    print("请输入一个正整数，您的输入有误")