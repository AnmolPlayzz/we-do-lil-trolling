n=3628800
a=1
for i in range(1,n+1):
    a*=i
    print(i, a)
print(a)
print("Length of the value:", str(len(str(a))))