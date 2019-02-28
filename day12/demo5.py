import math
lis = ['班长','学习委员','文化书记','纪律委员']
dict = {}
count = 1
list = []
try:
    while 1:
        name = input("请输入您的投票结果")
        if name in lis:
            list.append(name)
            for i in list:
                key = dict.get(i)
                if key == None:
                    dict[name] = 1
                else:
                    dict[name] += 1
            if name not in dict.get(name):
                print('$s 0票'%(name))
            Maxname = max(dict.values())
            print('最高票数是%d，得票人是%s'%(dict[Maxname],Maxname))
            dict[1::2] = sorted(dict[1::2],reverse=True)
except:
    print("您的投票无效")
