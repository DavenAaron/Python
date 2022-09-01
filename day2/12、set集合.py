# 无序、无key、无索引集合

# set 存放数据具有唯一性，去重
# 应用场景： 处理大量有重复信息的数据，对其去重；如果需要取值，将其转换为list
s = set()

# 增 (去重)
s.add('tom')
s.add('daven')
s.add('tom')

# 取值，遍历（set也提供了自身遍历）
ls = list(s)
print(ls)
for v in s:
    print(v)

# 多个关系set完成关系运算
py = {'a', 'b', 'c', 'daven'}
ln = {'x', 'y', 'z', 'daven'}
print(py - ln)

print('-------')
print(ln.difference(py))

print(ln & py)
print(ln ^ py)
print(py | ln)