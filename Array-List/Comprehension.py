#List comprehension is provide you a shortcut way to create a list from another iterable
#Set, Tuple, String, List,Dict is iterable

l1 = [x for x in range(11) if x%2==0]
print(l1)

def itr1():
    res = []
    for i in range(11):
        if i%2 ==0:
            res = res.append(i)
        print (res)




l2= [x for x in range(11) if x%2 !=0]
print(l2)


#Functions to get a list that contains all those items of l that are smaller than x

def getSmaller(l5,x2):
    return [e for e in (l5) if e<x2 ]

l5=[10,11,12,3,4,5,11]
x2=10
print(getSmaller(l5,x2))


def oddEven(list):
    even= [f for f in (list) if f%2==0]
    odd = [f for f in (list) if f%2 != 0]
    return even,odd

list=[10,3,20,4,5,12]
even,odd = oddEven(list)
print(even)
print(odd)

#Vowel print
s = "Ashutosh Pandey"
res2=[ x for x in s if x in "aeiou"]
print(res2)


l3=["geeks","ide","courses","gfg"]
res3=[x for x in l3 if x.startswith("g")]
print(res3)


l4=[x*2 for x in range(21)]   
print(l4)  #For each value of x in the range, the expression x*2 is evaluated. This means that each value of x is multiplied by 2.
#For x = 0, the expression evaluates to 0*2 = 0.
#For x = 1, the expression evaluates to 1*2 = 2.

l5=["ashutosh","pandey"]
res4=[ x.upper() for x in l5 if x.startswith("a") ]
print(res4)



#Two sets  #Distincts items  #no order

set = [10,20,3,4,10,20,7,3]
s1 = {x for x in set }
print(s1)

s2 = {x for x in set if x%2 == 0}
print(s2)

#Dict Comprehension
dict = [ 1,3,4,2,5]
d1 = { x : x for x in dict}
d2 = {x : x*3 for x in dict}
print(d1)
print(d2)




d3 = {x: f"ID{x}" for x in range(5)}
print(d3)


dict2=[101,103,102]
dict3=["ashu","pandey","python"]
d4 = {dict2[i]:dict3[i] for i in range(len(dict2))}
print(d4)


'''
This code creates a dictionary `d4` by pairing elements from `dict2` with elements from `dict3` based on their indices. Let's break it down step by step:

1. `dict2` is a list containing integers: `[101, 103, 102]`.
2. `dict3` is a list containing strings: `["ashu", "pandey", "python"]`.
3. `range(len(dict2))` generates the indices `[0, 1, 2]`, corresponding to the length of `dict2`.
4. For each index `i` in the range `[0, 1, 2]`:
   - `dict2[i]` accesses the element at index `i` in `dict2`, which will be `101`, `103`, and `102` respectively.
   - `dict3[i]` accesses the element at the same index `i` in `dict3`, which will be `"ashu"`, `"pandey"`, and `"python"` respectively.
5. The dictionary comprehension `{dict2[i]: dict3[i] for i in range(len(dict2))}` creates a dictionary where:
   - Each key is an element from `dict2` (at index `i`), and
   - Each value is the corresponding element from `dict3` (at index `i`).
6. Finally, `print(d4)` prints the resulting dictionary `d4`.

So, the output of this code will be:

```
{101: 'ashu', 103: 'pandey', 102: 'python'}
```

Each key-value pair in the dictionary represents an element from `dict2` paired with the corresponding element from `dict3`.

'''
