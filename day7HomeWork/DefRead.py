def Read(f,f2):
    file = open(f,'r')
    conten = file.readlines()
    file2 = open(f2,'w')
    for i in conten:
        file2.write(i)
    file2 = open(f2,'r')
    conten2 = file2.read()
    print(conten2)
    file.close()
    file2.close()

fileStr = input("请输入您想要拷贝的文件")
fileStr2 = input("现在请输入您想要拷贝到哪个文件中去")
Read(fileStr,fileStr2)
