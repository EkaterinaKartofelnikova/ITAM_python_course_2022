def summation(*args):
    mk=0
    k=0

    for i in args:
        if i<0:
            i=abs(i)*2
        if i>mk:
            mk=i
    for i in args:
        if i<0:
            i=abs(i)*2
            k=k+float(i/mk)
        else:
            k=k+float(i/mk)
    return(k)
print(summation(-10, 2, 3, 15, -4))





