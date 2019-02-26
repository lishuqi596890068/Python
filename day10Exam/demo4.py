# 使用while循环，实现持续的用户录入信息，将录入的信息以追加的方式保存至文件中，
# 当用户输入exit时，退出程序。（50分）
bool = True
msg = ''
while bool:
    name = input("请输入您的姓名")
    password = input("请输入您的密码")
    address = input("请输入您的住址")
    msg += '姓名是：'+name+'住址是：'+address
    f = open("user.txt",'w')
    f.write(msg)
    YorN = input("您是否还想要输入信息 y继续 or exit退出")
    if YorN == 'y':
        bool = True
    elif YorN == 'exit':
        bool = False
        print("成功退出程序")
