def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    else:
        piv = arr[0]
        less = [i for i in arr[1:] if i <= piv]
        greater = [i for i in arr[1:] if i > piv]
        return quick_sort(less) + [piv] + quick_sort(greater)

print(quick_sort([6,5,7,4,8,3,9,2,0,1]))

