#4.1
def arraySum(arr):
    if(len(arr) == 1):
        return arr[0]
    elif(len(arr) == 0):
        return None
    else:
        return arr[-1] + arraySum(arr[0:-1])

#4.2
def recLen(arr):
    if(len(arr) == 1):
        return 1
    elif(len(arr) == 0):
        return 0
    else:
        return 1 + recLen(arr[0:-1])

def maxarr(arr):
    if(len(arr) == 1):
        return 1
    elif(len(arr) == 0):
        return 0
    elif(len(arr) == 2):
        if(arr[0] > arr[1]):
            return arr[0]
        else:
            return arr[1]
    else:
        if(arr[0] > maxarr(arr[1:])):
            return arr[0]
        else:
            return maxarr(arr[1:])


print(arraySum(range(101)))
print(recLen(range(101)))
print(maxarr([1,2,3,4]))
