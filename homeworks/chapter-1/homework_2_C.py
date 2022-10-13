n = input()
a=0
b=0
c=0
s=[]
for i in range (len(n)):
    if n[i].isupper():
        a=i
        s.append(n[i])
        break
for i in range (len(n)-1):
    if n[i].isdecimal():
        b=i+1
        s.append(n[i+1])
        break
c=b-a
for i in range (b+3,len(n),3):
    s.append(n[i])
print(s)
