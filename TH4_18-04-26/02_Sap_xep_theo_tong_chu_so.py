import sys


def sum_digits(x):
    return sum(int(c) for c in str(x))


data = list(map(int, sys.stdin.read().replace("\ufeff", "").split()))
t = data[0]
i = 1

for _ in range(t):
    n = data[i]
    i += 1
    a = data[i : i + n]
    i += n
    a.sort(key=lambda x: (sum_digits(x), x))
    print(*a)
