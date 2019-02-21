# tel = input("请输入您的手机号")
# try:
#     int(tel)
#     list = ['135','138','159','158']
#     if(len(tel) == 11):
#         str = tel[:3]
#         if(str in list):
#             print("规范")
#         else:
#             print("不规范")
#
# except:
#     print("请输入正确的手机号")

import random
# list = []
# for i in range(50):
#     num = random.randrange(-10,10)
#     list.append(num)
# list1 = []
# list2 = []
# for i in list:
#     if i > 0:
#         list1.append(i)
#     elif i < 0:
#         list2.append(i)
# print(list1)
# print(list2)

# list = []
# for i in range(20):
#     num = random.randrange(20)
#     list.append(num)
# list[::2] = sorted(list[::2],reverse=True)
# print(list)


str = 'abcdefghi'
s = ''
for i in range(1000):
    s += random.choice(str)
print(s)
dict = {}
for i in s:
    key = dict.get(i)
    if(key == None):
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
