from math import cos, pi, sin

# Create a list of x values from -pi to pi, incrementing by 0.001
x_values = []
current_value = -pi
while True:
    x_values.append(current_value)
    current_value += 0.001
    if current_value > pi:
        break

h = 0.001

# Calculate the derivative of sin(x) for each x value
derivatives = []
cos_values = [] 
for x in x_values:
    derivative = (sin(x + h) - sin(x)) / h
    derivatives.append(derivative)
    cos_values.append(cos(x))

# Print each x value with its corresponding derivative and cos(x) value
for i in range(len(x_values)):
    print(f"x: {x_values[i]:.3f}, derivative: {derivatives[i]:.3f}, cos(x): {cos_values[i]:.3f}")