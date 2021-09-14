def min_sq(x, y):
    if(x % y == 0):
        return y
    else:
        if(x > y):
            return min_sq(y, x % y)
        else:
            return min_sq(x, y % x)


print(min_sq(80,80))
print(min_sq(640,1680))
print(min_sq(21,4))
