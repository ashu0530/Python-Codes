'''
I/P: l = [ 8,100,20,40,3,7]
 x = 10
O/P:  8,3,7
'''


def getSmall (l,x):
    small=[]
    for i in l:
        if i < x:
            #small+=[i]
           small.append(i) 
    return small




l = [8,100,20,40,3,7]
x = int(input())
print(getSmall(l,x))

