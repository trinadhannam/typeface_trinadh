n=int(input("Enter a Number:"))
a=0
b=1
while(a!=n):
    b=str(b)
    if ('3' not in b) and ('4' not in b) and ('7' not in b):
        a+=1
    b=int(b)
    b+=1
print(b-1)