
#Brute
def secondLargest2(l,n):
    l.sort(reverse=False)
    print(l)
    lar=l[n-1]
    print(lar)
    sec=-1
    for i in range(n-2,-1,-1):
        if l[i] !=lar:
            sec=l[i]
            break
    return sec


        
#Better
def secondLargest(l,n):
    largest=l[0]
    second=-1
    for i in range(1,n):
        if l[i] > largest:
            largest=l[i]
    for i in range(0,n):
        if l[i] > second and l[i] != largest:
            second=l[i]
    return second

#Optimal
def secondLargest3(l,n):
    largest=l[0]
    second=-1
    for i in range(1,n,1):
        if l[i] > largest:
            second=largest
            largest=l[i]
        else:
            if l[i] < largest and l[i] > second:
                second=l[i]
    return second


def sortedArray(l,n):
    for i in range(1,n,1):
        if l[i] > l[i-1]:
            return False
    return True

l = [90,45,64,33,44,22]
n = len(l)


print(secondLargest(l,n))
print(secondLargest2(l,n))
print(secondLargest3(l,n))
print(sortedArray(l,n))