def LCM(num1l, num2s):
    for i in range(1, num2s+1):
        if (num1l*i)%num2s == 0:
            return num1l*i
        else:
            pass

num1 =  int(input("Type first number"))
num2 = int(input("Type second number"))
if num1 > num2:
    print(LCM(num1, num2))
else:
    print(LCM(num2, num1))
