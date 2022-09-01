# 1、声明
s1 = '字符串'
s2 = "字符串"
s3 = """多行
字符串"""

## 字符串嵌套： 完成有引号的字符串输出
## 转义： \

print("""\"小名\"
同学""")

# 二、字符串索引取值
s2 = 'abc123哈哈'
#正向索引， 从0开始编号
print(s2[3])
# 反向索引，从-1开始编号
print(s2[-3])

# 三、切片（获取子字符串，语法：[startindex:stopindex:step]
# 结束索引：-1代表截图到最后以为之前，省略代表截取到最后
# 开始索引：省略标识从开头截取
# 步长： 复数时从后开始截取
s = 'haha jerry'
print(s[2:4:1])
print(s[1::])
print(s[:-1:])

# 四、长度
s3 = 'abdce'
print(len(s3))

# 五、拆分 就是将字符串转化为列表 rsplit |split
# str.split(str="", num=string.count(str))
s4 = "D:\\home\pkg\mysqld.gz"
s4_list = s4.split('\\')
print(s4_list)
print(s4_list[-1])

# 五、成员判断 in| not in
s5 = 'abc123哈哈'
print('abc' in s5)
print('abd' not in s5)

# 六、首尾去白
s6 = ' helo world '
print(s6.split())

# 七、数字判断 isdigit
# num = input("input：")
# if num.isdigit():
#     num = int(num)
#     print(num)
# else:
#     print("input nums")
#
# while True:
#     num = input("input：")
#     if num.isdigit():
#         num = int(num)
#         print(num)
#         break
#     else:
#         print("input agen")

# reStr  = ''
# count = 0
# while True:
#     num = input("input %s: " % reStr)
#     if num.isdigit():
#         num = int(num)
#         print(num)
#         break
#     elif count >= 3:
#         print("too many erros!")
#         break
#     else:
#         print("input nums")
#         reStr = "agen"
#         count += 1

