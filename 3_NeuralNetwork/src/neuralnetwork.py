#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
import time

def step_function(x):
    print(f"[step_function] {x}")
    y = x > 0
    print(f"[step_function] {y}")
    return y.astype(np.int)

def plot_step_function():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # y軸の範囲を指定
    plt.show()

if __name__ == '__main__':
    plot_step_function()
