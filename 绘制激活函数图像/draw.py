import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0,x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def draw():
    x1 = np.arange(-10, 10, 0.1)
    y1 = sigmoid(x1)
    plt.subplot(1,2,1)
    plt.plot(x1, y1)
    plt.grid()
    plt.title('(a) Sigmoid', y=-0.15)

    x2 = np.arange(-10, 10, 0.1)
    y2 = relu(x2)
    plt.subplot(1, 2, 2)
    plt.plot(x2, y2)
    plt.title('(b) ReLU', y=-0.15)
    plt.grid()

    plt.show()

if __name__ == '__main__':
    draw()