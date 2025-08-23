def arrayTotalSum(a):

    lenght = len(a)

    if lenght == 1:
        return a[0]
    
    return a[0] + arrayTotalSum(a[1:])

a = [34, 23,-41,1]

print("Array total sum: ",arrayTotalSum(a))