def secondLargest(a,n):
    largest=a[0]
    slargest=-1

    for i in range(1,n,1):
        if a[i]>largest:
            slargest=largest
            largest=a[i]
        else:
            if a[i]<largest and a[i]>slargest:
                slargest=a[i]
    return slargest

def secondSmallest(a,n):
    smallest=a[0]
    ssmallest=99999

    for i in range(1,n,1):
        if a[i]<smallest:
            ssmallest=smallest
            smallest=a[i]
        else:
            if a[i] !=smallest and a[i] < ssmallest:
                ssmallest=a[i]
    return ssmallest




def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    slargest=secondLargest(a,n)
    ssmallest=secondSmallest(a,n)
    return slargest, ssmallest
    pass
