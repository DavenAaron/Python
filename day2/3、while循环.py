
# count = 0
# while count < 10:
#     print(count)
#     count +=1
#

res = 1
num = 1

while num <= 100:
   if num % 7 == 0:
        res = num
   num +=1

print(res)


# break： 用来结束所属的最近一层循环
# 从大到小循环可以快速找到98

res = 100
num = 100
while num >= 1:
    if num % 7 == 0:
        res = num
        break
    num -= 1
print(res)
print('-------------')
# countinue: 结束本次循环（中断屏蔽当次循环的逻辑下方代码），进入下一次循环

# 打印所有三十岁一下的年龄
ages = [18, 32, 20, 35, 27, 25]
count = 0
while count < 6:
    if ages[count] < 30:
        print(ages[count])
    count += 1

print('---while.else---')
# while...else....: 当循环没有被break打断，else分支才会被执行
count = 0
while count < 5:
    print(count)
    # break
    count += 1
else:
    print("循环合理结束")