import math
from equation import bisection, newton_raphson

if __name__ == '__main__':
    f1 = lambda x: x - math.cos(x)
    print(bisection(f1, 0, 1, 10e-12))

