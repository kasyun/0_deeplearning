import sys
import os
from PIL import Image
import numpy as np
from neuralnetwork import sigmoid, softmax
import pickle
import datetime


def load_dataset():
    sys.path.append("../../deep-learning-from-scratch/")
    from dataset.mnist import load_mnist
    (x_train, t_train), (x_test, t_test) = load_mnist(
        flatten=True,
        normalize=False,
        one_hot_label=False
    )

    return (x_train, t_train), (x_test, t_test)


def get_data():
    return load_dataset()[1]


def init_network():
    with open("../../deep-learning-from-scratch/ch03/sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


def calc_mnist():
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            accuracy_cnt += 1
    print(f"Accuracy: {str(float(accuracy_cnt) / len(x))}")


def print_mnist():
    (x_train, t_train), (x_test, t_test) = load_dataset()
    print(x_train.shape)
    print(t_train.shape)
    print(x_test.shape)
    print(t_test.shape)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    # pil_img.show()
    print(f"{pil_img.format, pil_img.size, pil_img.mode}")
    pil_img.save('sample.jpg', quality=95)


def plot_mnist():

    (x_train, t_train), (x_test, t_test) = load_dataset()
    position = 0
    img = x_train[position]
    label = t_train[position]
    print(f"selected image[{position}] label = {label}, shape = {img.shape}")
    img = img.reshape(28, 28)
    print(f"image new shape = {img.shape}")

    img_show(img)


if __name__ == '__main__':
    start = datetime.datetime.now()
    # print_mnist()
    # plot_mnist()
    calc_mnist()
    end = datetime.datetime.now()
    print(f"elapsed time = {end - start}")
