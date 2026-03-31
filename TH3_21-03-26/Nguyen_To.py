import sys

def phi(n):
    kq, i = n, 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0: n //= i
            kq -= kq // i
        i += 1
    if n > 1: kq -= kq // n
    return kq

def nt(n):
    if n < 2: return 0
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return 0
        i += 2
    return 1

a = list(map(int, sys.stdin.buffer.read().split()))
print('\n'.join('YES' if nt(phi(n)) else 'NO' for n in a[1:]))