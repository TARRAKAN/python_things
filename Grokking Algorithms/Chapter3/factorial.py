def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

for i in range(1, 11):
    print(fact(i))
