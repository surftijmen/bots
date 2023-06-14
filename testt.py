import numpy as np
import matplotlib.pyplot as plt

learningrate = 0.1
epochs = 20

#Input and target values for OR and AND functions
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
ors = np.array([0, 1, 1, 1])
ands = np.array([0, 0, 0, 1])
xors = np.array([0, 1, 1, 0])

#activation function
def step(x):
    return np.where(x >= 0, 1, 0)

def perceptron(inputs, targets):
    weights = np.zeros(inputs.shape[1])
    bias = 0
    errors = []
    print("perceptron")
    for epoch in range(epochs):
        total_error = 0
        for input, target in zip(inputs, targets):
            output = step(np.dot(input, weights) + bias)
            error = target - output
            # update weigth and bias
            weights += learningrate * error * input
            bias += learningrate * error
            # add error to total error for this epoch
            total_error += np.abs(error)
            print(total_error)

        #Normalize erro
        errors.append(total_error / inputs.shape[0])

    return errors

# train all 3 functions
or_error = perceptron(inputs, ors)
and_error = perceptron(inputs, ands)
xor_error = perceptron(inputs, xors)

# Plot everything
plt.figure(figsize=(10, 5))

# OR
plt.subplot(1, 3, 1)
plt.plot(or_error)
plt.title('OR')
plt.xlabel('Epoch')
plt.ylabel('Total error')
plt.ylim([-0.2, 1.2])

# AND
plt.subplot(1, 3, 2)
plt.plot(and_error)
plt.title('AND')
plt.xlabel('Epoch')
plt.ylabel('Total error')
plt.ylim([-0.2, 1.2])

# XOR
plt.subplot(1, 3, 3)
plt.plot(xor_error)
plt.title('XOR')
plt.xlabel('Epoch')
plt.ylabel('Total error')
plt.ylim([-0.2, 1.2])

plt.show()