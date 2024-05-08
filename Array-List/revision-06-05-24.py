




#Optimized one - second Largest
def secondLargest(l,n):    
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

#BruteForce
def secondLargest2(l,n):
    l.sort(reverse=False)
#    print(l)
    largest=l[n-1]
#    print(largest)
    second=-1
    for i in range(n-2,-1,-1):
        if l[i] !=largest:
            second=l[i]
            break
    return second

#better
def largest(l,n):
    max=l[0]
    for i in range(1,n,1):
        if l[i] > max:
            max=l[i]
    return max
def secondLargest3(l,n,max):
    slargest=-1
    for i in range(0,n,1):
        if l[i] > slargest and l[i] != max:
            slargest=l[i]
    return slargest

#duplicates in sorted array #Two pointer approach
def removedDuplicates(l,n):
    l.sort(reverse=False)
#    print(l)
    firstPointer=l[0]
    temp=[]
    for i in range(1,n,1):
        if l[i] != firstPointer:
            temp=temp.append(i)
    return temp


#Check is array is sorted or not
def isSorted(l,n):
    for i in range(1,n,1):
        if l[i-1] < l[i]:
           return True
        else:
            return False
        

#left rotate by one place

def leftRotateByOne(l,n):
    temp=l[0]
    #print(temp)

    for i in range(1,n,1):
        l[i-1]=l[i]
    l[n-1] = temp
    return l

#BruteForce approach
def leftRotateByD(l,n,d):
#    print(l)
    d = d%n
#    print(d)    
    temp=l[0:d]
#    print(temp)
    
    for i in range(d,n,1):
        l[i-d]=l[i]

    for i in range(n-d,n,1):
        l[i]=temp[i-(n-d)]    
    return l

#Another brute
def leftRotateByD2(l,n,d):
    d = d%n   
    temp=l[0:d]
    
    for i in range(d,n,1):
        l[i-d]=l[i]

    j = 0
    for i in range(n-d, n, 1):
        l[i]  = temp[j]
    return l 
    
 #Direct method
def leftRotateByD3(l,n,d):
    l = l[d:] + l[:d]
    return l       

#Optimised way
#def leftRotatebyD4(l,n,d):


l = [1,2,3,4,5,6]
n=len(l)
max=largest(l,n)
d=2
l2=l.reverse()
print(l2)

print("Second Largest element is:",secondLargest(l,n))
print("Second Largest element is:",secondLargest2(l,n))
print("Second Largest element is:",largest(l,n),secondLargest3(l,n,max))
print("Check array is sorted", isSorted(l,n))
print("Left rotate by one place", leftRotateByOne(l,n))
print("Left rotate by d place", leftRotateByD(l,n,d))
print("Left Rotate by d place another brute method", leftRotateByD2(l,d,n))
print("Left Rotate by d place another brute method", leftRotateByD3(l,d,n))
