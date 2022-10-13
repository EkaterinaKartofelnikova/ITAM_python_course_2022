n = int(input())
a = []
k=0
p=0
for i in range(n):
    a=(input().split(" "))
    if a[-1]=="True":
        k+=1
    else:
        p+=1
print(k,p)



