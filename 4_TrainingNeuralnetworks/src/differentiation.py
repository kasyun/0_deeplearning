import numpy as np


def numerical_diff(f, x):
    # h = 1e-50
    h = 1e-4
    # return (f(x + h) - f(x)) / h
    return (f(x + h) - f(x - h)) / (2 * h)


def diff_test_function(x):
    """y = 0.01x^2 + 0.1x
    """
    return 0.01 * x**2 + 0.1 * x


def main():
    print(diff_test_function(5), numerical_diff(diff_test_function, 5))
    print(diff_test_function(10), numerical_diff(diff_test_function, 10))


if __name__ == '__main__':
    main()
