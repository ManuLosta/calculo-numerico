def bisection(f, a, b, error):
    mid = (a + b) / 2
    i = 0
    while abs(b - a) > error:
        if i > 100000:
            return Exception("No solution found")

        fa, fb = f(a), f(b)
        mid = (a + b) / 2
        print(f"n: {i} | a: {a} | b: {b} | p{i}: {mid} | f(a): {fa} | f(b): {fb} | f(p{i}): {f(mid)}")

        if f(mid) * fa < 0:
            b = mid
        elif f(mid) * fb < 0:
            a = mid

        i += 1

    return mid


def newton_raphson(f, fd, x0, error):
    x = x0 - f(0) / fd(x0)
    i = 0
    while i <= 1000000:
        xn = x - f(x) / fd(x)
        if abs(f(xn)) < error:
            return xn

        x = xn

    return Exception("No solution")