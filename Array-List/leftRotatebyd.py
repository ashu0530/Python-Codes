

def rotateArraybyd(l,n,d):
    d = d%n   #modulos
    n=len(l)
    temp = l[:d]
    print(temp) #Store first 3 element which is d in temp variable

    for i in range(d,n,1):
        l[i-d]=l[i]
    #print(l)

    for i in range(n-d,n,1):
        l[i] = temp[i-(n-d)]
    #print(l)
    return l




l = [1,2,3,4,5,6,7]
n=len(l)
d=3
print("Length of array:", n)
print(rotateArraybyd(l,n,d))