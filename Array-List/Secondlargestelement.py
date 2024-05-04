'''
input = arr[] = [10,5,8,20]
output = 10
input = arr[] = [10,10,10]
output = None
'''


#bruteforce approach - 1st sort the array
#Nlogn+n is Time complexity

def secondLargest(l):

    if len(l)<2:
        return "Array must have atleast 2 values"
    
    l.sort()    #1,2,4,5,7,7
    print("Sorted array:", l)
    largest=l[-1]  #7
    print("Largest Value:", largest)
    i = len(l)-2  #7
    print(i)
    
    
    while i>=0:     #loop run till i not become zero
        if l[i] != largest:    
            return l[i]
        i = i-1    
l = [1,2,4,7,7,5]
print("Second largest element:", secondLargest(l))


#If you put res = l[i] and return res on the same line within the loop, it would mean that the function will immediately return the first element that is greater than the initial res, without checking the rest of the elements. Therefore, it will only consider the second element 2 
#Optimal one Time complexity = o(n) first pass second pass o(n) which *is o(2n)
def max(l):
    res=l[0]
    if len(l)<2:
        return "array should have atleast 2 value"
    for i in range(1, len(l)):
        if l[i] > res:
            res = l[i]
    return res

def SecondMax(l,max_value):
    slargest=-1
    for i in range(0,len(l)):
        if l[i] > slargest and l[i] != max_value:
            slargest=l[i]
    print(slargest)


l = [1,2,4,7,7,5]
max_value=max(l)
print("Max value is:", max_value)
SecondMax(l, max_value)

#best one
def secondL(l):
    largest=l[0]
    second = -1
    for i in range(1,len(l)):
        if l[i] > largest:
            second = largest
            largest=l[i]
        elif l[i] < largest and l[i] > second:
            second=l[i] 
    return second



l = [1,2,4,7,7,5]
print("Second largest value is: " , secondL(l))


'''
Sure, let's go through the iteration step by step with the provided `secondL` function and the list `[1, 2, 4, 7, 7, 5]`.

1. **Initialization**:
   - `largest` is initialized with the first element of the list, which is `1`.
   - `second` is initialized with `-1`, indicating that it hasn't found the second largest yet.

2. **Iteration**:

    - **Iteration 1**:
        - `i = 1`, `l[1] = 2`.
        - `l[1]` is less than `largest` (which is `1`), so it's not greater.
        - `l[1]` is greater than `second` (which is `-1`), so `second` becomes `2`.

    - **Iteration 2**:
        - `i = 2`, `l[2] = 4`.
        - `l[2]` is less than `largest` (which is still `1`), so it's not greater.
        - `l[2]` is greater than `second` (which is `2`), so `second` becomes `4`.

    - **Iteration 3**:
        - `i = 3`, `l[3] = 7`.
        - `l[3]` is greater than `largest` (which is `1`), so `second` becomes `largest` (which is `1`) and `largest` becomes `l[3]`, which is `7`.

    - **Iteration 4**:
        - `i = 4`, `l[4] = 7`.
        - `l[4]` is equal to `largest` (which is `7`), so it's not greater.
        - It doesn't enter the second condition because `l[4]` is not less than `largest`.

    - **Iteration 5**:
        - `i = 5`, `l[5] = 5`.
        - `l[5]` is less than `largest` (which is `7`), so it's not greater.
        - `l[5]` is greater than `second` (which is `1`), so `second` becomes `5`.

3. **Return Value**:
   After the loop, `second` holds the second largest value found during the iteration, which is `5`.

So, the `secondL` function iterates through the list once, keeping track of the largest and second largest elements encountered. At the end of the iteration, it returns the second largest element found.

'''