import numpy as np


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


def main():
    y2 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    y7 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.5, 0.0]
    t2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    t7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

    y2 = np.array(y2)
    y7 = np.array(y7)
    t2 = np.array(t2)
    t7 = np.array(t7)

    print(mean_squared_error(y2, t2))
    print(mean_squared_error(y7, t2))

    print(cross_entropy_error(y2, t2))
    print(cross_entropy_error(y7, t2))


if __name__ == '__main__':
    main()
