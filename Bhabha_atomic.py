n=int(input())

s=0
for i in range(1,n):
    if n%i==0:
        s+=i
    else:
        continue
if s==n:
    print("perfect")
else:
    print("non perfect")