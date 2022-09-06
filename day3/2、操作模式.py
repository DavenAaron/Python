'''
主模式：
r: 文件必须存在读
w: 文件无需存在的写， 无创建, 有清空再写
a: 文件无需存在的写，无创建， 有在文件最后追加写

从模式：
t: 按文本字符操作数据（默认模式）
b: 按文本字节操作数据
+： 可读可写

'''

# with open 语法
# 操作系统对于文件的支持全由with
with open('/tmp/test3.txt', 'r', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())

# 追加模式
with open('/tmp/test3.txt', 'a+') as f:
    f.write('tomcat')
    f.write('dave\n')
    f.write('end\n')
    data=f.read()
    print(data)

# 字节方式操作文件
# b操作模式下不需要指定encoding
# 数据在硬盘中本就是以二进制进行存储，所有b操作就是对数据从硬盘到内存的拷贝
# 但如果数据需要展现给用户，文件文件就要涉及到解码，其他文件需要
with open('/tmp/test3.txt', 'rb') as f:
    data = f.read()
    print(data)
    print(data.decode('utf-8'))

print('--------')
with open('/tmp/test4.txt', 'a+') as f:
    f.write('嘿嘿')
    data = f.read()
print(data)