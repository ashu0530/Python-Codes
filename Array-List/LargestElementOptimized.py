#linear time solution


def getMax(l):
    if not l:
        return None
    else:
        res=l[0]    #initialise result with first element be best case
        for i in range(1,len(l)):
            if l[i]> res:
                res = l[i]
            return res
l = [10,20,5,2]
print(getMax(l))


#without len function
def getMax(l):
    if not l:
        return None
    else:
        res=l[0]    #initialise result with first element be best case
        length=0
    for x in l:
            length+=1        #count to find the length
    for i in range(1,length):
        if l[i]> res:
            res = l[i]
        return res
l = [10,20,5,2]
print(getMax(l))