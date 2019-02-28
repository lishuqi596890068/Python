list = ['班长','学习委员','纪律委员','文化书记']
dict = {}
import math

while 1:
    name = input("请输入您的投票")
    if name in list:
       key = dict.get(name)
       if key == None:
        dict[name] = 1
       else:
        dict[name] +=1
    bool = input("您是否还想要继续投票")
    if bool == '结束':
        break
Max = max(dict.values())
for i in dict:
    if Max==dict[i]:
       Maxname = dict.get(i)

print('票数最高的是%s,票数是%d'%(Maxname,Max))
for i in list:
    if i not in dict.keys():
        print('%s得票数是0'%(i))
dict = sorted(dict.items(),key = lambda x:x[1],reverse=True)

print(dict )


