print([3] in [1,2,3])
print('ab' in 'acbd')
print('=======')
num = set([1,2,2,4])
#存值到set中 并且可以利用set特性进行去重
print(type(num))
print(len(num))
print('=========')


class parent:
    def __init__(self,param):
        self.v1 = param
class child(parent):
    def __init__(self,param):
        self.v2 = param
obj = child(11)
print('%d %d'%(obj.v2,obj.v2))
print('============')
num = 14
print(num>>2)
print('=====')
import re
phone = '2004-959 # 这是一个电话号码'
num = re.sub(r'#.*$','',phone)
print('电话号码',num)
print('======')
print(set([1,2,3]) == {1,2,3})
print(type(set([1,2,3])))
print(type({1,2,3}))
print('=======')
print(3<5>2)
print('==============今日20k作业=============')
# 编写程序，生成一个包含20个随机整数的列表，
# 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，奇数下标的元素不变。（提示：使用切片。）
import random
list = []
for i in range(20):
    list.append(random.randrange(50))
print(list)
list[::2] = sorted(list[::2],reverse=True)
print(list)
print('====================')

# 2.随机生成一个包含1000个字母的字符串
# ，然后统计该字符串中每个字母的数量，并输出结果（要求结果以字典方式存储）
strList = 'abcdefg'
str = ''
for i in range(1000):
    str += random.choice(strList)
print(str)
dict = {}
for i in str:
    key = dict.get(i)
    if key == None:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
print('==========')

# 3.实现以下功能：
# 	(1)编写一个函数，该函数的功能是在输入列表中查找大于50的元素，并将大50的前10个元素以列表方式返回
# （如果满足要求的元素不足10个，就有几个返回几个）；
# 	(2)编写一个函数，该函数的功能是在输入列表中查找所有的5的倍数，并将结果以列表方式返回；
# 	(3)随机生成一个包含1000个整数（范围为1-100）的列表，然后测试你编写的以上两个函数。
def find(list):
    ten = []
    count = 0
    for i in list:
        if i > 50:
            ten.append(i)
            count += 1
            if count == 10:
                break
    print(ten)


def bei(list):
    wu = []
    for i in list:
        if i % 5 ==0:
            wu.append(i)
    print(wu)
    
l = []
for i in range(1000):
    l.append(random.randrange(1,100))
find(l)
bei(l)




