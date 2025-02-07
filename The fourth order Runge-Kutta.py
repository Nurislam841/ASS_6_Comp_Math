def runge_kutta4(f, x, y, h, steps):
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        print(f"x: {round(x, 2)}, y: {round(y, 5)}")
    return y

def equation(x, y):
    return x + y

x_start = 0
y_start = 1
h = 0.1
steps = 2

runge_kutta4(equation, x_start, y_start, h, steps)