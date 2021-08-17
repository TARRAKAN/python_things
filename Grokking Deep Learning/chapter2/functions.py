def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    output = list()
    for i in range(len(vec_a)):
        output.append(vec_a[i] * vec_b[i])
    return output

def elementwise_addition(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    output = list()
    for i in range(len(vec_a)):
        output.append(vec_a[i] + vec_b[i])
    return output

def vector_sum(vec_a):
    output = 0
    for num in vec_a:
        output += num
    return output

def vector_averege(vec_a):
    output = 0
    for num in vec_a:
        output += num
    return output/len(vec_a)

print(elementwise_multiplication([1,2,3], [4,5,6]))
print(elementwise_addition([1,2,3], [4,5,6]))

print(vector_sum([1,2,3]))
print(vector_averege([1,2,3]))

