import math
from equation import bisection, newton_raphson

if __name__ == '__main__':
    f1 = lambda x: x-2**(-x)
    f1d = lambda x: 1 + math.log(2)*2**(-x)
    print(newton_raphson(f1, f1d, -0.5, 10e-8))

