import math
import sys


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


data = list(map(int, sys.stdin.read().replace("\ufeff", "").split()))
if data:
    n, m = data[0], data[1]
    k = 2
    for _ in range(n):
        row = data[k : k + m]
        k += m
        print(*[1 if is_prime(x) else 0 for x in row])
