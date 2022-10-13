def summation(start,next):
    k=0
    if start < next:
        while start<=next:
            k+=start
            start+=1
    else:
        while next<=start:
            k+=next
            next+=1
    return(k)
start,next=map(int,input().split( ))
print(summation(start,next))
