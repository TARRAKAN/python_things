import numpy as np

ih_wgt = np.array([
                [ 0.1,  0.2, -0.1],
                [-0.1,  0.1,  0.9],
                [ 0.1,  0.4,  0.1]])

hp_wgt = np.array([
            [0.3, 1.1, -0.3],
            [0.1, 0.2,  0.0],
            [0.0, 1.3, 0.1]
            ])

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes = 8.5
wlrec = 0.65
nfans = 1.2

input = np.array([toes, wlrec, nfans])

pred = neural_network(input, weights)
print(pred)
print(np.array([1,2,3]).dot([1,1,1]) )
