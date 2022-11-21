str1=input("Enter a String:")
str2=input("Enter a String:")
a=str2[len(str2)-1]
n=0
for i in str1:
    if a==i:
        n+=1
print(n)