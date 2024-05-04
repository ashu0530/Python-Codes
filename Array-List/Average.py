#Average or mean of a list
# I/P: l = [10,20,30,40,50]
#O/P : 25.0
#steps we need to store first the result of this so create variable
#iterate through whole list we use loop , and saving every iteration on i variable
# to stop the loop

def avg(l):
    sum = 0
    for i in l:
      sum = sum+i
    n = len(l)
    
    return sum / n

l = [10,20,30,40,50]
print (avg(l))