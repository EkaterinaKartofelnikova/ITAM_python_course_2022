n = input().split(" ")
a=[]
a.append(n[-1])
for i in range (len(n)-1):
    a.append(n[i])
print(" ".join(a))