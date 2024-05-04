#Two pointer approach

def duplicates(l,n):
    i=0
    for j in range(1,n,1):
        if l[j] != l[i]:
            l[i+1] = l[j]
    return 







l = [1,2,3,4,5,6,6,7,7,8]
n=len(l)