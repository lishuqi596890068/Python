#从一个文件中的图片拷贝到另一个文件中去
def copy(str1,str2):
    f = open(str1,'rb+')
    conten = f.read()
    ff = open(str2,'wb+')
    print(conten)
    ff.write(conten)
    f.close()
    ff.close()
s1 = input("从哪个文件中拷贝图片")
s2 = input("拷贝到哪个文件中去")
copy(s1,s2)




