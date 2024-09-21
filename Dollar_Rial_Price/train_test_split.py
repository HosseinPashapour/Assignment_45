import numpy as np
import pandas as pd


def train_test_split(x, y, test_size=.2):
    # Shuffle the indices
    indices = np.arange(len(x))
    np.random.shuffle(indices)

    # Calculate the index to split the data
    split_index = int((1 - test_size) * len(x))

    # Split the data
    x_train, x_test = x[indices[:split_index]], x[indices[split_index:]]
    y_train, y_test = y[indices[:split_index]], y[indices[split_index:]]

    return x_train, x_test, y_train, y_test


