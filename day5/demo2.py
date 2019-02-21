# 用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可
# .判断手机号码是否是由数字组成的(总分15分，5分能够判断是否为数字，
# 5分判断是否为有效号段，5分实现)

tel = input("请输入您的手机号")
try:
    int(tel)
    list = ['135','138','159','158','166']
    if(len(tel)==11):
        print("您的手机号是11位，没错")
        str = tel[:3]
        if(str in list):
            print("您的手机号前三位符合规范")
        else:
            print("但是您的手机号前三位不符合规范")
except:
    print("请输入正确的手机号")




# 2. 编写程序，生成一个包含50个随机整数的列表，
# 随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，
# 负数存为另一个新的子列表。
# （15分：生成随机列表5分，得出正负数新列表各5分）


import random
list = []
for i in range(50):
    num = random.choice(range(-10,10))
    list.append(num)
print(list)
listZ = []
listF = []
for i in list:
    if i > 0:
        listZ.append(i)
    elif i < 0:
        listF.append(i)
print("正数列表",listZ)
# print("负数列表",listF)



#
# 编写程序，生成一个包含20个随机整数的列表，
# 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
# 奇数下标的元素不变。（提示：使用切片。） (20
# 分：生成列表5分，找到偶数下标8分，降序7分)
import random
list = []
for i in range(20):
    num = random.randrange(20)
    list.append(num)
print(list)
#使用切片，然后找到偶数下标 利用sorted方法 参数中可以设置reverse是True 注意是大写的T进行翻转
list[::2] = sorted(list[::2],reverse=True)
print(list)





# 随机生成一个包含1000个字母的字符串，
# 然后统计该字符串中每个字母的数量，并输出结果（要求结果以字典方式存储）
# （20分
# ：随机生成字符串5分，统计字母数量8分，以字典方式存储5分，输出结果2分）
import random
str = 'abcdefg'
s = ''
for i in range(1000):
    s += random.choice(str)
print(s)
dict = {}
for i in s:
    key = dict.get(i)
    #利用字典的键值对特性 键是唯一的 看看字典中是否存在dict.get(i)
    #利用这个元素获得键 键如果是None 代表没有这个键，将其值等于一
    if(key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)



s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \
#将这个字符串分割 利用他的空格进行分割
s = s.split(' ',s.count(' ')-1)
#分割的时候可以控制分割几次 注意到字符串的末尾有个空格，我们不去分割这个
#计算出了总共有多少个空格以后，将其减一
print(s)
dict = {}
for i in s:
    key = dict.get(i)
    if (key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
list = dict.values()
print(list)