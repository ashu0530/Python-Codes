

#Bruteforce convert array to set because set having the distinct value




def duplicate(l):
    # Create a set to store unique elements
    unique_set = set()
    # Initialize an empty list to store duplicate elements
    duplicates = []
    
    # Iterate through the list
    for item in l:
        # If the element is already in the set, it's a duplicate
        if item in unique_set:
            # Append the duplicate to the duplicates list
            duplicates.append(item)
        else:
            # Otherwise, add it to the set of unique elements
            unique_set.add(item)
    
    # Return the list of duplicate elements
    return duplicates

l = [1, 1, 2, 3, 3, 4, 5]
print("Duplicate values are:", duplicate(l))



#Two pointer apporach

def duplicate_2(l2):
    i = 0
    res = []
    for j in range(1,len(l2)):
        if l2[j] != l2[i]:
            l2[i+1]==l2[j]
            i+=1
            
    



l2 = [1, 1, 2, 3, 3, 4, 5]
print("Duplicate values are:", duplicate_2(l2)) 