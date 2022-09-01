
# 空列表 ， 只包含一个值（元素、成员）的列表
l1 = []
l2 = [1]
print(l1, l2)

# 元组： 可以理解为不可变的列表，
# 1、元组的长度不可以变化，
# 2、但是值可以变化，但变化实际是存放了可变的数据类型，元组本地没有改变

# 一、定义
t1 = ([123, 2, 13, 2, 12])
print(t1)

# tuple 将列表转换为元组
t2 = tuple([1, 2, 3])
print(t2)

# 空元组
t4 = tuple()
print(t4)

# 含一个值的元组
t5 = (1, )
print(t5)

t6 = tuple((1, ))
print(t6)

# 不可改变： 但一个列表需要对其进行限制，让其无法发生改变，可以将其转化为元组
list1 = [1, 2, 3]
tuple1 = tuple(list1)
print(tuple1)

list1 = list(list1)
print(list1)

# 注： 元组中存放了可变类型数据，可以发生形式上的值改变，本质值未发生改变
t1 = (1, 'abc', [10, 'xys'])
print(t1, id(t1))

t1[2][1] = 'WWW'
print(t1, id(t1))

