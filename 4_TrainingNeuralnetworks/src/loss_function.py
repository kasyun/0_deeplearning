import numpy as np
import sys


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # delta = 1e-7
    # return -np.sum(t * np.log(y + delta))
    batch_size = y.shape[0]
    print(f"[cross_entropy_error] batch size = {batch_size}")
    return -np.sum(t * np.log(y)) / batch_size
    # return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size


def test_loss_function():
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


def test_mnist():
    (x_train, t_train), (x_test, t_test) = load_dataset()
    print(x_train.shape)
    print(t_train.shape)
    train_size = x_train.shape[0]
    batch_size = 10
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]


def load_dataset():
    sys.path.append("../../deep-learning-from-scratch/")
    from dataset.mnist import load_mnist
    (x_train, t_train), (x_test, t_test) = load_mnist(
        # flatten=True,
        normalize=True,
        one_hot_label=True
    )

    return (x_train, t_train), (x_test, t_test)


def main():
    test_loss_function()
    # test_mnist()


if __name__ == '__main__':
    main()
