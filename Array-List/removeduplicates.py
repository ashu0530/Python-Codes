#Two pointer approach

def duplicates(l,n):
    i=0
    for j in range(1,n,1):
        if l[i] != l[j]:
            i+=1
            l[i]=l[j]
    return i+1







l = [1,2,3,4,5,5,6,7,7]
n=len(l)
print(duplicates(l,n))