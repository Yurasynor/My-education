a = int('2454')
mult = 1
while (a != 0):
    mult = mult * (a % 10)
    a = a // 10
print("result: ", mult)


a = int('2454')
n = 0
while a > 0:
    z = a % 10
    a //= 10
    n *= 10
    n += z
print(n)

a = 2454; 
c = str(a); 
x = list(c); 
a = sorted (c)
print(a)