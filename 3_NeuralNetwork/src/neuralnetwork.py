#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
import time
import sys


def step_function(x):
    """Activation function: Step Function.
    """
    print(f"[step_function] {x}")
    y = x > 0
    print(f"[step_function] {y}")
    return y.astype(np.int)


def sigmoid(x):
    """Activation function: Sigmoid.
    """
    return 1 / (1 + np.exp(-x))


def relu(x):
    """Activation function: ReLU.
    h(x) = x (x > 0), h(x) = 0 (x <= 0)
    """
    return np.maximum(0, x)


def identity_function(x):
    """Actication function: Identity mapping
    """
    return x


def softmax(a):
    """Activation function: Softmax.
    for classification.
    """
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def plot_function(activation_type: str):
    x = np.arange(-5.0, 5.0, 0.1)
    if "sigmoid" in activation_type:
        y = sigmoid(x)
    elif "relu" in activation_type:
        y = relu(x)
    else:
        y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
    plt.show()


def plot():
    args = sys.argv
    _activation_type = "None" if len(args) < 2 else args[1]
    print(
        f"activation_type = {_activation_type} [step_function(default), sigmoid, relu]")
    plot_function(_activation_type)


def inner_product_3_3_2():
    A = np.array([[1, 2], [3, 4], [5, 6]])
    print(A, A.shape)
    B = np.array([7, 8])
    print(B, B.shape)
    print(np.dot(A, B))


def inner_product_3_3_3():
    X = np.array([1, 2])
    print(X, X.shape)
    W = np.array([[1, 3, 5], [2, 4, 6]])
    print(W, W.shape)
    Y = np.dot(X, W)
    print(Y)


def neuralnetwork_3_4_2():
    x = np.array([1.0, 0.5])
    res = forward(init_network(), x)
    print(f"input = {x}, output = {res}")


def forward(network, x):
    W1, W2, W3 = network["w1"], network["w2"], network["w3"]
    B1, B2, B3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + B1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + B2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + B3
    y = identity_function(a3)

    return y


def init_network():
    network = {}
    network["w1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["w2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["w3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


if __name__ == '__main__':
    # plot()
    # inner_product_3_3_3()
    # neuralnetwork_3_4_2()
    a = np.array([1010, 1000, 990])
    print(softmax(a))
