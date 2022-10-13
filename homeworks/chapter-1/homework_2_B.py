n = int(input())
k = 0 #очные
p = 0 #заочные
s = 0
for i in range(n):
    a=input().split(" ")
    if a.count("False" and "True")==1:
        if a.count("False")==1:
            p+=1
        else:
            k+=1
    elif a.count("False" or "True")>1:
        if a[-1]=="False":
            p+=1
        elif a[-1]=="True":
            k+=1
    else:
            s+=1
print(k,p,s)