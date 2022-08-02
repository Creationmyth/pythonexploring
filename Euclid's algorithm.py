def HCF(highest, lowest):
    r = highest % lowest
    if r == 0:
        return lowest
    elif r > 0:
        return HCF(lowest, r)

number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
if number1 > number2:
    print(HCF(number1, number2))
else:
    print(HCF(number2, number1))