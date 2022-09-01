a = 10
print(a)

# 交换数量整型数的值
a = 10
b = 20
c = a
a = b
b = c
print(a, b)

# 交叉负值
a = 10
b = 20
a, b = b, a
print(a, b)

# 运算赋值
num = 100
num += 1  # num = num + 1
num **=2
num //=2

#解压赋值
list = [1, 2, 3, 4, 5]
a = list[1]
b = list[2]
c = list[0]
print(a, b, c)

# 按位赋值
list = [1, 2, 3, 4, 5]
a, b, c, d, e = list
print(a, b, e)


# 只得到首位两个
list = [1, 2, 3, 4, 5]
x, _, _, _, y = list
print(x, y, _)