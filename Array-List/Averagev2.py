#Without len function

def avg(l):
    sum = 0
    count=0  #length = 0
    for i in l:
      sum = sum+i
      count=count+1
    
    return sum / count

l = [10,20,30,40,50]
print (avg(l))