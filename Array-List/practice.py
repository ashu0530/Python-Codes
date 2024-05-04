#Largest element in array



def largest(l):
    if len(l) < 1:
        print("Enter more value in list")
    res = l[0]
    for i in range(1,len(l)):
        if l[i] > res:
           res=l[i]
    return res




l = [10,20,30,40,15]
print("Max value is", largest(l))


#check array is sorted 

def sorted(l2):
    i = 1
    while i < len(l2):
        if l2[i] < l2[i-1]:
            return False
        i = i+1
    return True
l2=[10,20,30,10,1]
print(sorted(l2))

def sorted2(l3):
    for j in range(1,len(l3)):
        if l[j] < l[j-1]:
            return False
        j = j+1
    return True

l3=[10,20,30,10,1]
print(sorted2(l3))

#odd only 


def evenOdd(l4):
    even=[]
    odd=[]

    for i in l4:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd




l4=[10,2,3,4,5,6,7,8,9,1]
print(evenOdd(l4))



#find only odd only

def odd(l5):
    res = []
    for i in range(0,len(l5)):
        if i % 2 != 0:
            res.append(i)
            
    return res


l5=[10,2,3,4,5,6,7,8,9,1]
print(odd(l5))