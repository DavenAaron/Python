# # 算数运算符
# print(10 + 10)
#
# # 字符串  +（字符串拼接） *（字符串重复）
# s = 'da'
# end = 'ven'
# name = s + end
# print(name)
# print(s+end)
# print(name*3)
#
# # % 取余（求模）| ** 指数（求幂）| //整除 | /除法
# print(5 % 2)
# print(5 ** 2)
# print(5 // 2)
# print(5 / 2)
#
# # 比较运算符 < > == !=
# res = 5 !=4
# print(res)
#
# res = 5 > 19
# print(res)
#
# # 判断一个值是否大于3小于5
# num = input("input a num:")
# print(type(num))
# # 将str的num转换为int的num
# num= int(num)
# print(type(num))
# # 可以连比
# print(5 > num > 4)
#
# # 逻辑运算符
# # and| or | not
# print(5 > num and num > 3)
# print( 40 > num or num > 199)

# 逻辑运算符的短路现象
# and前为假，整个表达式为假，后边不用判断被短路
# or前为真，整个表达式为真，后边不用判断被短路
res = 1 and 0 or 3
print(res)

print("10" == 10)


# == 与 is的比较区别
# == 只做值比较，is做id比较