#I/p: 10,20,30,40
#O/P: 20,30,40,10

#by pop and append direct method
def leftRotate(l):
    l.append(l.pop(0))
    return l


l = [10,20,30,40]
print(leftRotate(l))

#by logic

def leftRotate2(l2):
    n = len(l2)  #4
    x = l[0]  #10 

    for i in range(1,n):
        l2[i-1]=l2[i]
    l2[n-1] = x
    




l2 = [10,20,30,10]
print(leftRotate2(l2))


