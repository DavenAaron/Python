# 游标操作 一定要做b模式下进行操作，因为游标一定按字节进行偏移
# seek（偏移量，操作位置）
# 操作位置：0 从头开始，1 从当前位置开始，2从最后开始


# fileObject.seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

# f.seek(5,0)    # 从开始往后偏移五个字节
# f.seek(-1, 1)   # 从当前位置向前便宜一个字节
# f.seek(1, 1)  # 从当前位置向后偏移一个字节
# f.seek(-5, 2)  # 从末尾向前偏移五个字节

# with open('/tmp/test5.txt', 'rt', encoding='utf-8') as f:
#     f.seek(1,2)
#     d2 = f.read()
#     print(d2)

# seek在操作位置为0时， 可以兼容t模式，但仍然按字节进行偏移
print('----')
fo = open("/tmp/runoob.txt", "a+")
print ("文件名为: ", fo.name)
l1 = fo.read()
print(l1)

line = fo.readline()
print ("读取的数据为: %s" % line)

# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print ("读取的数据为: %s" % line)

# 关闭文件
fo.close()

print('---关闭文件---')
f1 = open("/tmp/f1.txt", 'r')
# f1.write('my\nname\nis\ndaven')
f1.seek(2, 0)
position = f1.tell()
print(position)
print(f1.read())

print(' ------ ceshi ----- ')
f2 = open('/tmp/file2.txt', 'w+')
f2.write('www.baidu.com\nwwww.jd.com\nwww.zengui.wang')
f2.seek(0)
print(f2.read())


print('-------')
with open('/tmp/python/change.txt', 'rb+') as f:
    f.seek(10, 0)
    print(f.tell())
    f.write(b'age:18')
    f.seek(0)
    print(f.read())

