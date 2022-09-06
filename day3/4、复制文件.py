# 复制文件
'''
name:Owen
age:18
gender:God
'''
with open('/tmp/python/change.txt', 'r', encoding='utf-8') as f1, open('/tmp/python/new.text', 'w', encoding='utf-8') as f2:
    for line in f1:
        print(line)
        f2.write(line)