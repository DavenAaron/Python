# lstrip | rstrip： 左右去留白
s1 = " hello world "
print(s1.lstrip())
print(s1.rstrip())

s2 = "*** hello world ===="
print(s2.lstrip("*"))
print(s2.rstrip("="))

# rsplit: 从右开始拆分
s3 = "D:\\home\pkmg\python3.gz"
s3_list = s3.split("\\", 2)
print(s3_list)

# lower | upper : 大小写
print("AAAACd".lower())
print("dddSWFf".upper())

# 4、startswith | endswith： 以某某开头|结尾 返回值为bool类型
print("http://www.baidu.com".startswith('https://'))
print("http://www.baidu.com".endswith('baidu.com'))

# 5、format： 格式化
print('name: %s, age: %s' % ('daven', '18'))
print('name: {}, age: {}' .format('daven', '188'))
# 占位要与实际数据进行个数与位置的匹配
print('name: {0}, age:{1}'.format("tomcat", 46))
print('name: {ns}, age:{ae}'.format(ns="tomc", ae=416))

# 6、replace： 替换
# 语法： replace(oldS, newS, count)
s6 = 'abcaDeaaafG'
print(s6.replace('a', 'A', 2))

# 7、find | rfind: 查找子字符串索引，返回第一次查询到的索引 无结果返回-1，
s1 = 'abcdedfa'
print(s1.find('d'))
print(s1.rfind('d'))

# 8、index | rindex ： 查找子字符串索引，无结果抛出异常
print(s1.index('a', 2, 8))

# 9、count： 计算子字符串个数
print(s1.count('a'))

# 10、center | ljust | rjust | zfill
print(s1.center(30, '-'))
print(s1.ljust(30, '-'))
print(s1.rjust(30, '-'))
print(s1.zfill(30))

# 11、captialize | title | swapcase ： 首字母、单词首字母，大小写反转
print('hello world'.capitalize())
print('hello world'.title())
print('hello world'.swapcase())

# 12、isdigit | isdecimal | isnumeric  数字、小数、罗马数判断
# 13、isalnum | isalpha ： 是否由字母数字组成 | 由字母组成
print('abc123'.isalnum())
print('123'.isalpha())

# 14、isidentifier 判断字符是否是合法变量名
print('a_123'.isidentifier())

# 15、islower | isupper ： 是否全小|大写
print('abc'.isupper())
print('abc'.islower())

# 16、 isspace： 空白字符
print('tomcat'.isspace())
print(' '.isspace())

# 17、istitle： 是否为单词首字母大写格式
print('tomcat'.istitle())
print('Tomcat'.istitle())

