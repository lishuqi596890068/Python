import random
argStr = 'ABCD'
str = ''
list = []
for i in range(1,501):
     if i<10:
         str = 'S0000%d'%(i)
         list.append(str)
     elif i>=10 and i<100:
         str = 'SOO0%d'%(i)
         list.append(str)
     elif i>=100:
         str = 'SOO%d'%(i)
         list.append(str)
print(list)
arg = ''
dict = {}
for i in list:
    arg = i
    key = dict.get(arg)
    boo = False
    str2 = ''
    for k in range(50):
        if boo == False:
            str2 += random.choice(argStr)
    boo = True
    if boo == True:
        dict[i] = str2
print(dict)


f = open('num.txt','w')
filename = ''
for k in range(500):
    filename = '%s %s'%(list[k],dict.get(list[k]))
    print(filename)
    f.write(filename)
f = open('num.txt','r')
conten = f.readline()
f.close()











