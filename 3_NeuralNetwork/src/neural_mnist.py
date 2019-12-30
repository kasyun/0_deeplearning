import sys
import os
from PIL import Image
import numpy as np


def load_dataset():
    sys.path.append("../../deep-learning-from-scratch/")
    from dataset.mnist import load_mnist
    (x_train, t_train), (x_test, t_test) = load_mnist(
        flatten=True,
        normalize=False,
        one_hot_label=False
    )

    return (x_train, t_train), (x_test, t_test)


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
    # print_mnist()
    plot_mnist()
