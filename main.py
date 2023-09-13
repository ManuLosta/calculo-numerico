import math
from equation import bisection, newton_raphson

if __name__ == '__main__':
    f1 = lambda x: math.e**(-x) - x + 2
    print(bisection(f1, 2, 3, 10e-15))