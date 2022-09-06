
# 编码： ascii unicode gbk gb2312 utf-8


s1 = 'tomcat hahah'
# 编码
res = s1.encode('utf-8')
print(res)

# 解码
s2 = res.decode('utf-8')
print(s2)