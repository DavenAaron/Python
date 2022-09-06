
# 操作文件的三步骤
#1、打开文件
f = open('/tmp/file.txt', 'r', encoding='utf-8')

# 2、操作文件

# read() 函数：逐个字节或者字符读取文件中的内容；
# readline() 函数：逐行读取文件中的内容；
# readlines() 函数：一次性读取文件中多行内容。

print(f.read()) # 读所有内容

# 3、关闭文件
#f.close()     # 操作系统对文件的持有权一定要在文件操作完毕后释放
f = open('/tmp/file.txt', 'r', encoding='utf-8')
print('------')
# print(f.read())
# print(f.read(5))

# 读取指定字节数或者字符数
print(f.read(1))

# 按行将所有行一次取出到list中
f1 = f.readlines()
print(f1)
print(type(f1))

# 写入文件
# 文件基本操作模式： w, 文件不存在就新建，存在就清空
# 1、按字符进行操作
# 2、write('写入第一行\n写入第2行\n')
# 3、flush() 将之前写入内存的数据刷新到磁盘中
# 4、writelines(list) list中存放一条条的文件内容，需要明确\n标识换行 writelines(['1111\n', '2222\n'])
print('--1-----')
w = open('/tmp/file1.txt', 'w', encoding='utf-8')
# w.write('123')
# w.write('haha')
# w.flush()
#w1=w.readlines()
# w1 = w.read()
print(type(w))
w.write('123')
w = open('/tmp/file1.txt', 'r', encoding='utf-8')
print(w.read())


w = open('/tmp/test3.txt', 'w', encoding='utf-8')
w.writelines(['one\n', 't\n'])
w = open('/tmp/test3.txt', 'r', encoding='utf-8')
print(w.read())

