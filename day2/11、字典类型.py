# 字典

# 一、声明
dic1 = {'name': 'daven', 'age': 18}
print(dic1)

dic2 = dict([('name', 'age'), ('daven', 18)])
print(dic2)

# 二、get 存在就会打印实际的值，不存在未规定默认值则返回None
print(dic1.get('name1', '该key不存在'))

# 三、字典的key可以为所以不可变类型， value可以为任意类型
d1 = {}.fromkeys([1, 3.14, (1,), '123', True], None)
print(d1)

# 四、增删查改
dic = {'name': 'daven', 'age': 18}
print(dic)

# 增
dic['gender'] = 'man'
print(dic)

# 删
del dic['age']
print(dic)

# 改
dic['name'] = 'jerry'
print(dic)

# 查
print(dic['name'])

# 设置默认值， 没有该key添加并设置默认值,如果有 则不对其操作
dic = {'name': 'daven', 'age': 18}
dic.setdefault('from', 'sd')
print(dic)

# 通过keys初始化字典
dic = dic.fromkeys(['name', 'from', 'age'], None) # 设置默认值 一般为None
print(dic)

# 多值类型
dic = {'name': 'daven', 'age': 18}
dic.update({'name': 'tom', 'from': 'qd'})
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

for k in dic.keys():
    print(k, ':', dic[k])

for k, v in dic.items():
    print(k, ':', v)


print('---------')
dic = {
    'students':[
        {
            'name': 'daven',
            'id': 1,
            'from': 'sd'
        },
        {
            'name': 'tom',
            'id': 2,
            'from': 'qd'
        }

    ],
    'teachers':[]
}

print(dic.items())
for k, v in dic.items():
    print(k, v)

print(dic['students'][1]['name'])

print('-------')
for k, v in dic.items():
    if k == 'students':
        for stu in v:
            for s_k, s_v in stu.items():
                print(s_k, ':', s_v)
            print('------')
