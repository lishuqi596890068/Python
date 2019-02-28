
try:
    print("=========打开文件===========")
    with open('fruit.txt','r') as f:
        conten = f.readlines()
        print(type(conten))
        i = 1
        for temp in conten:
            print('%d %s'%(i,temp))
            i += 1
        position = f.tell()
        print('文件指针位置',position)
        #seek有两个参数 第一个偏移量 第二个是方向 0 从文件头开始计算 1 从当前位置开始 2 从文件的末尾
        f.seek(6,0)
        position = f.tell()
        print('现在指针的位置是',position)
        conten = f.read()
        print('从第五字节开始读取',conten)
        import os
        #创建文件夹
        os.mkdir('张三')
        #获取当前目录
        print(os.getcwd())
        os.listdir('./')
        os.rmdir('张三')




except FileNotFoundError as e:
    print("文件未找到")
    print(e)
except UnicodeDecodeError as e:
    print(e)

