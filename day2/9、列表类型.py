# 1、定义列表
l1 = [1, 3.12, 53, 'abc']
print(l1)

# 二、字符串 列表处理
# 将字符串转换为列表
print('hahhaha'.split('h'))
# 将列表转换为字符串
print('.'.join(["21", "3", "tom"]))

# 三、切片
list3 = [1, 2, 3, 4, 5]
print(list3[1:-1:2]) #[2, 4]

# 四、增删改查
#删除普通变量
# a = 10
# del  a
# print(a)

# 增
list4 = []
list4.append(5)
list4.append(10)
print(list4)

# 插入
list4.insert(0, 110)
print(list4)

# 删
# 删除指定索引
del list4[0]
print(list4)

# 删除指定对象
list4.remove(5)
print(list4)

# 改
list4[0] = 10000
print(list4)

# 查
list5 = [1, 33, 41, 1]
print(list5)
print(list5[1])

# 五、长度
print(len(list5))

# 六、成员运算
print(2 in list5)

# 七、循环：迭代
list7 = ['m', 'y', 'n', 'a', 'm', 'e']
print(type(list7))
# for obj in list7:
#     print(obj,end=',')
print(' '.join(list7))

print('--------')
list8 = ["11", "23", "1", "3","1"]
l8 = '.'.join(list8)
print(l8)
print(type(l8))


# 翻转
a = [1, 3, 2]
a.reverse()
print(a)

# 排序 sort： 数据之间全部具有可比性，要统一类型
b = [5, 3, 112, 1, 32]
b.sort(reverse=True)
print(b)

x = [1, 3, 5]
y = x
print(x,id(x))
print(y,id(y))

z = x.copy()
print(z, id(z))

# clear 清空
# count 计算成员个数
# extend 添加多个值

list1 = []
list1.extend([1, 4])
print(list1)
list2 = ['abc', 'xrz']
list1.extend(list2)
print(list1)