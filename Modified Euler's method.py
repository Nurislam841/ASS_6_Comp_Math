def modified_euler(f, x, y, h, steps):
    for _ in range(steps):
        slope1 = f(x, y)
        y_predict = y + h * slope1
        slope2 = f(x + h, y_predict)
        y = y + (h / 2) * (slope1 + slope2)
        x += h
        print(f"x: {round(x, 2)}, y: {round(y, 5)}")
    return y

def equation(x, y):
    return 1 - y

x_start = 0
y_start = 0
h = 0.1
steps = 3

modified_euler(equation, x_start, y_start, h, steps)