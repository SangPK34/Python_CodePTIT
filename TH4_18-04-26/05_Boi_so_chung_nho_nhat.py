import sys

MOD = 10**9 + 7


def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            step = i
            start = i * i
            is_p[start : n + 1 : step] = [False] * ((n - start) // step + 1)
    return [i for i in range(2, n + 1) if is_p[i]]


def exp_in_fact(n, p):
    e = 0
    while n:
        n //= p
        e += n
    return e


data = list(map(int, sys.stdin.read().replace("\ufeff", "").split()))
if data:
    t = data[0]
    tests = [(data[i], data[i + 1]) for i in range(1, 2 * t, 2)]
    max_b = max(b for _, b in tests)
    primes = sieve(max_b)

    for a, b in tests:
        ans = 1
        for p in primes:
            if p > b:
                break
            e = exp_in_fact(b, p) - exp_in_fact(a - 1, p)
            if e:
                ans = (ans * (2 * e + 1)) % MOD
        print(ans)
