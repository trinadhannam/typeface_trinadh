n=int(input("Enter the size of the matrix:"))
rec=[]
for i in range(n):
    rec.append(map(int,input()))
print(rec)
a=0
b=n-1
for i in range(len(rec)):
    if 0 not in rec[i]:
        a+=1
    else:
        break
for i in range((len(rec))):
    if 0 not in rec[n-1-i]:
        b-=1
    else:
        break
print(a,b)
x=a
y=b
c=n-1
d=0
while(x<=b):
    for i in range(len(rec[a])):
        if rec[x][i]==0:
            if c>i:
                c=i
    x+=1
    for i in range(len(rec[a])):
        if rec[y][n-i-1]==0:
            if d<(n-i-1):
                d=n-i-1
    y-=1
print(a,b)
print(a,d)
print(b,c)
print(c,d)
        