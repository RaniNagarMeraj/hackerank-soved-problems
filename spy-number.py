n=int(input().strip())
lst=[int(digit)for digit in str(n)]
s=sum(lst)
p=1
for digit in lst:
    
    p*=digit
    
if s==p:
    print("spy")
else:
    print("not spy")