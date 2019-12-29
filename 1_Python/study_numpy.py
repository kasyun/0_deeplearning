import numpy as np


def main():
    np_1_5_4()


def np_1_5_4():
    a = np.array([[1, 2], [3, 4]])
    """
    [[1 2]
    [3 4]], (2, 2), int32
    """
    print(f"{a}, {a.shape}, {a.dtype}")

    b = np.array([[3, 0], [0, 6]])
    """
    [[ 4  2]
    [ 3 10]]
    [[ 3  0]
    [ 0 24]]
    """
    print(a + b)
    print(a * b)


def np_1_5_3():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 4.0, 6.0])
    """
    output
    [3. 6. 9.]
    [-1. -2. -3.]
    [ 2.  8. 18.]
    [0.5 0.5 0.5]
    """
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)

    # broadcast
    # [0.5 1.  1.5]
    print(x / 2.0)


if __name__ == '__main__':
    main()
