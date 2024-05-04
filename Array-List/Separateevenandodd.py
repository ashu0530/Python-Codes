#I/P: [10,41,30,15,80]
#O/P: even = [10,30,80]
#     odd = [ 41, 15]


def evenOdd(l):
    even=[]  #empty list
    odd=[] #empty list
    for i in l:
        if i%2==0:
            #even.append(i) same functionalities
            #even = even+[i]
            even +=[i]
        else:
            #odd.append(i) same functionalities
            #odd = odd+[i]
            odd +=[i]
    return even,odd


l = [10,41,30,15,80]
even,odd=evenOdd(l)
print(even)
print(odd)