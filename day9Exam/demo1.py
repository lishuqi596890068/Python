# 输入一个字符串，将该字符串反顺序输出（40分）
# str = input('请输入一个字符串')
# # for i in range(len(str)):
# #     print()
# print(str[::-1])
#
#
# # 编写函数求三角形面积，输入参数为底边与高，输出面积（20分）
# def s(d,h):
#     mian = d*h*1/2
#     print('三角形面积是',int(mian))
# di = int(input('请输入三角形的底'))
# gao = int(input('请输入三角形的高'))
# s(di,gao)

nums = set([1,1,2,3,3,3,4])
print(len(nums))
f = open('str.txt','w')
f.write('aaaaaa')
f = open('str.txt','r')

content = f.readline()
print(type(content))