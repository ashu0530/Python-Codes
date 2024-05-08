#Brute Force
def moveAllZero(arr,n):
    temp=[]

    for i in range(n):
        if arr[i] !=0:
            temp.append(arr[i])
    
    for i in range(len(temp)):
        arr[i] = temp[i]
    #return arr

    for i in range(len(temp),n):
        arr[i] =0
    return arr





arr=[1,0,2,3,2,0,0,4,5,1]
n=len(arr)
print(moveAllZero(arr,n))
