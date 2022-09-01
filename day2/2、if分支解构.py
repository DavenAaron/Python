# 顺序解构
# age = int(input('input your age:'))
#
# # if 语法
#
# if age <= 18:
#     print("孩子")

# age = int(input('input your age:'))
# if age <= 18:
#     print('孩子')
# else:
#     print('老男人')

# age = int(input('input your age: '))
# if age < 18:
#     print('孩子')
# elif age > 80:
#     print('老人')
# else:
#     print('青年')

username = input('input your name: ')
if username == 'daven':
    print('账号存在，正在认证密码.....')
    passwd = input('input your passwd: ')
    if passwd == '123':
        print('登录成功')
    else:
        print('密码错误，退出登录！')
else:
    print('账号不存在，请重新输入！')