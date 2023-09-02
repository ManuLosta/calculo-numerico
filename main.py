import math
from equation import bisection, newton_raphson

if __name__ == '__main__':
    f1 = lambda x: x ** 4 - 2 * x ** 3 - 4 * x ** 2 + 4 * x + 4
    fd1 = lambda x: 4 * x ** 3 - 6 * x ** 2 - 8 * x + 4
    f2 = lambda x: x - math.exp(-x)

    print(bisection(f1, -2, 0, 0.00000001))
    print(bisection(f1, 0, 2, 0.00000001))
    print(bisection(f1, 1, 2, 0.00000001))
    print(bisection(f1, -1, 0, 0.00000001))

    print(newton_raphson(f1, fd1, 0, 0.00000001))
