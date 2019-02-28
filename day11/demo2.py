with open('fruit.txt','w') as f:
    f.write('娃哈哈')
    f.write('你说呢')
    f.writelines('换行' + '\n')
    f.writelines('再换一行'+'\n')
with open('fruit.txt','r') as f:
    conten = f.read()
    print(conten)