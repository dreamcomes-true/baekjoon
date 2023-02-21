num1 = int(input())
num2 = input()
#num1 = 472
#num2 = '385'

num3 = num1*int(num2[2])
num4 = num1*int(num2[1])
num5 = num1*int(num2[0])
num6 = num3 + num4*10 + num5*100
print(num3)
print(num4)
print(num5)
print(num6)