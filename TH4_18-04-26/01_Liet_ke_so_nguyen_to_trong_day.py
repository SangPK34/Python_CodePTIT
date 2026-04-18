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


s = sys.stdin.read().replace("\ufeff", "").split()
if s:
    n = int(s[0])
    a = list(map(int, s[1 : 1 + n]))

    cnt = {}
    order = []
    for x in a:
        if is_prime(x):
            if x not in cnt:
                order.append(x)
                cnt[x] = 0
            cnt[x] += 1

    for p in order:
        print(p, cnt[p])
