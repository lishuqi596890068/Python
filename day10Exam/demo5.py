# 使用with打开fruit.txt文件，
# 写入‘Other health benefits of this master juice combo include。’（2
with open('fruit.txt','w') as f:
    f.write('Other health benefits of this master juice combo include')
with open('fruit.txt','r') as f:
    conten = f.read()
    print(conten)
with open('fruit.txt','w') as f:
    f.write('Anti-inflammatory and Nerve-calming Juice Recipe')
with open('fruit.txt','r') as f:
    print(f.read())
