## 变量三要素
* 1、变量值： 变量名
* 2、变量地址： id(变量名)
* 3、变量类型：type(变量名)


## 标识符命名规范
1、可以由字母、下划线组合
2、不能以数字开头
3、不能与系统关键字保留字重名
4、见名知意，建议使用_连接语法，一般下划线开头或结尾都有特殊含义

```python
name = input('input your name:')
gender = input('input your gender:')
age = input('input your age:')

print(''' ------ starting ------
name: %s
gender： %s
age: %s
------ end ------
''' % (name, gender, age))
```

# 数据类型 int、float、bool、list、dict
```python


# int
age = 18
print(age, type(age))

# float
salary = 8888.9
print(salary, type(salary))

#bool: True/False
result = False
print(type(result))

# list: 存放多个数据
list_1 = ['tom',  'jerry', 'daven']
print(list_1, type(list_1))

# list嵌套
list_3 = [
    ['tom', 'cat'],
    ['mm', 'dd'],
]
print(list_3, type(list_3))

# dict: key-value
dic= {
    'name': 'daven',
    'age': 18,
}
print(dic, type(dic))
```