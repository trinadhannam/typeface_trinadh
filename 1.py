n=int(input("Enter a Number:"))
a=""
while(n!=0):
    d=n%3
    d=str(d)
    a=d+a
    n=n//3
print(a)
    