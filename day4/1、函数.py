# 函数： 用来完成特定功能的代码，减少代码冗余，解构更加清晰，提高复用性

'''
语法：
def 函数名（参数列表）：
    函数体
    return 返回值
'''


# 函数四部分
'''
1、函数名： 使用该函数的依据
2、函数体： 完成功能的代码块
3、返回值： 功能完成的返回结果
4、参数： 完成功能需要的条件信息
'''

# 购物案例
def shoping(money, goods):
     print('花了%s,买了个%s' % (money, goods))
     print('花了{},买了个{}' .format(1000, 'iphone18'))

shoping(100, 'iphone')

'''
三种字符串：
    u：普通的
    b： 二进制
    r： 原义字符串

编码： u''.encode('utf-8')
解码： b''.decode('utf-8')

转换：
    str(b'', encode='utf-8')
    bytes(u'', encode='utf-8')
'''