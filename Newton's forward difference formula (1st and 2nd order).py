import numpy as np


def newton_forward_difference(x, y):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    print(diff_table)
    return diff_table


def first_derivative(x, diff_table, h):
    return (diff_table[0, 1] - (diff_table[0, 2] / 2) + (diff_table[0, 3] / 3)) / h


def second_derivative(x, diff_table, h):
    return (diff_table[0, 2] - diff_table[0, 3] + (11 / 12) * diff_table[0, 4]) / h ** 2


x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([0, 6, 20, 42, 72], dtype=float)
h = x[1] - x[0]

diff_table = newton_forward_difference(x, y)
f_derivative = first_derivative(x, diff_table, h)
s_derivative = second_derivative(x, diff_table, h)

print("First derivative at x0:", f_derivative)
print("Second derivative at x0:", s_derivative)