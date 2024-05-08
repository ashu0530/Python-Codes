#Optimal #Two pointer approach
def moveAllZero(arr,n):
    #Find Zeroth Element
    
    
    zeroth = -1
    for i in range(n):
        if arr[i] == 0:
            zeroth=i
            break

    if zeroth == -1:
        return arr
    
    for i in range(zeroth+1,n):
        if arr[i] 
        

            

arr=[1,0,2,3,2,0,0,4,5,1]
n=len(arr)
print(moveAllZero(arr,n))