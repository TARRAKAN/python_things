def binary_search(list, item):
    low = 0
    high = len(list)-1

    while(low <= high):
        mid = low + high
        guess = list[mid]
        if(guess == item):
            return mid
        if(guess > item):
            high = mid - 1
        else:
            low = mid + 1
    return None

lst1 = [1,3,5,7,9,11]
print(binary_search(lst1, 1))
print(binary_search(lst1, 3))
print(binary_search(lst1, 5))
print(binary_search(lst1, 7))
print(binary_search(lst1, 9))
print(binary_search(lst1, 11))
print(binary_search(lst1, 222))

#1.1 log(2)128 = 7
#1.2 7+1
