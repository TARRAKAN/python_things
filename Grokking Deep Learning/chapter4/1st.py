
knob_weight = 1.5
input = 0.5 
goal_pred = 0.8

pred = input * knob_weight

error = (pred - goal_pred) ** 2

print(error)
