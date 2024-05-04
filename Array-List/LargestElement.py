'''
input = l = [10,5,20,8]
output = 20
input = l = [ 40]
output = 40
'''


def largest(l):
    for x in l:  #iterate first 
        for y in l:  #check every iteration  
            if y > x:
                break
        else:
            return x
    return None


l = [10,5,20,8]
print(largest(l))