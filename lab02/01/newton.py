from functions import f1, f2


def Newton(f, a, b, eps):
    iterations = 0

    x_current = a
    if f1(x_current) * f2(x_current) <= 0:
        x_current = b

    x_next = x_current - f(x_current) / f1(x_current)

    while abs(x_current - x_next) >= eps:
        x_current = x_next
        x_next = x_current - f(x_current) / f1(x_current)
        iterations += 1

    return x_next, iterations
