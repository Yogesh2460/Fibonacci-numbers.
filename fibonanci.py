a=0
b=1
print(a)
print(b)
n=int(input("enter the number of Fibonacci numbers you want."))
for i in range(n):
    c=a+b
    a,b=b,c
    print(c)
