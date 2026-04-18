import sys


def prod_digits(x):
    p = 1
    for c in str(x):
        p *= int(c)
    return p


data = list(map(int, sys.stdin.read().replace("\ufeff", "").split()))
t = data[0]
i = 1

for _ in range(t):
    n = data[i]
    i += 1
    a = data[i : i + n]
    i += n
    a.sort(key=lambda x: (prod_digits(x), x))
    print(*a)
