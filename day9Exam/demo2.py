# 编写函数，判断输入参数字符串是否为邮箱地址，检验条件为：
# 字符串中间用@分隔，末尾是.com或者.net（40分）
def email(str):
    print(str[-4:])
    if str.count('@')==1:
        if str[-4:]=='.com' or str[-4:] == '.net':
            print("邮箱地址正确")
        else:
            print("请输入正确的邮箱地址")
    else:
        print("请输入正确的邮箱地址包括@符号")

s = input("请输入您的邮箱地址")
email(s)
#
# 编写程序，包含try…except…else …finally
# 各个分支内语句,通过调用测试每个分支运行正确（20分）
num = input("请输入一个数字")
try:
    int(num)
except:
    print("请输入一个数字")
else:
    num = 5
finally:
    print(num)
    print("这个数字不一定是5")