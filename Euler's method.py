def euler_method(func, x_start, y_start, step_size, x_target):
    x_current = x_start
    y_current = y_start

    while round(x_current, 5) < x_target:
        slope = func(x_current, y_current)
        y_next = y_current + step_size * slope
        x_next = x_current + step_size

        print(
            f"x: {round(x_current, 2)}, y: {round(y_current, 2)}, slope: {round(slope, 2)} -> new y: {round(y_next, 2)}")
        x_current, y_current = x_next, y_next
    return y_current

def differential_equation(x, y):
    return x + y

x_initial = 0.0
y_initial = 1.0
h = 0.1
x_final = 1.0

approximate_y = euler_method(differential_equation, x_initial, y_initial, h, x_final)

print()
print("Approximated value of y in x=1:", round(approximate_y, 2))