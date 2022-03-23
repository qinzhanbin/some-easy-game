import random
num = random.randint(1,100)
n = 1
m = 100
while True:
    x = input("输入一个数字\nEnter a number：")
    y = int(x)

    if y == num:
        print("炸弹来咯~\nThe bomb to cough up")
        print("乖乖接受惩罚吧\nJust accept your punishment")
        break

    else:
        #print(num)
        if y < num:
            if n < y:
                print('%d~%d'%(y,m))
                n = y
            else:
                print('不可以这样哦,请重新说一个数字\nYou cant do that,Please re-enter')
        else:
            if y < m:
                print('%d~%d'%(n,y))
                m = y
            else:
                print('不可以这样哦,请重新说一个数字\nYou cant do that,Please re-enter')

        #print(n)
        #print(m)
