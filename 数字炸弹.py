import random
num = random.randint(1,100)
n = 1
m = 100
while True:
    x = input("说出一个数字：")
    y = int(x)

    if y == num:
        print("炸弹来咯~")
        break

    else:
        #print(num)
        if y < num:
            if n < y:
                print('%d~%d'%(y,m))
                n = y
            else:
                print('不可以这样哦,请重新说一个数字')
        else:
            if y < m:
                print('%d~%d'%(n,y))
                m = y
            else:
                print('不可以这样哦,请重新说一个数字')

        #print(n)
        #print(m)
