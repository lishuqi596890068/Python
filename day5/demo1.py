alist = [1,2,3,4]
alist.reverse()
print(alist)
print("=============")
print('123'**3)

import random
list = []
for i in range(20):
    num = random.randrange(20)
    list.append(num)
print(list)
list[::2] = sorted(list[::2],reverse=True)
print(list)

print("=============")
tel = input("请输入您的手机号")
list = ['135','159','158','153','138']
try:
    int(tel)
    if(len(tel)==11):
        print("您的手机号是十一位")
        str = tel[:3]
        print(str)
        if(str in list):
            print("您的手机号符合规范")
        else:
            print("您的手机号不符合要求")

except:
    print("请输入正确的手机号")

print("=============")
import random
list = []
for i in range(50):
    num = random.randrange(-10,10)
    list.append(num)
zheng = []
fu = []
for i in list:
    if i > 0:
        zheng.append(i)
    elif i < 0:
        fu.append(i)
print(zheng)
print(fu)

print("=============")
import  random
str = 'abcdefg'
s = ''
for i in range(1000):
    s += random.choice(str)

dict = {}
for i in s:
    key = dict.get(i)
    if(key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)



print("=============")
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \

s = s.split(' ',s.count(' ')-1)
dict = {}
print(s)
for i in s:
    key = dict.get(i)
    if(key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
list = dict.values()
print(list)


