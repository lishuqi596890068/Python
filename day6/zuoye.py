f = open('src.txt','w')
f.write('你是谁呢')
f.write('不要管我是谁')
f.write('来我家玩吧')
f.write('好的呀')
f = open('src.txt','r')
conten = f.read ()
print(conten)
f = open('dst.txt','w')
f.write(conten)

def fun(a=5,b=10,c=15):
    print(a+b+c)
fun(a=15,b=5)

