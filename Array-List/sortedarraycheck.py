#check array is sorted or not





def sorted(l):
    i = 1
    while i < len(l):
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True


def sorted2(l):
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True




        








l = [1,2,2,3,3,4]
print(sorted(l))
print(sorted2(l))