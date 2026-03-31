import sys, math

def nt(n):
    if n < 2: return 0
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return 0
        i += 6
    return 1

a = sys.stdin.read().split()
t = int(a[0])
kq = []
for i in range(1, t + 1):
    n = int(a[i])
    s = str(n)
    tong = 0
    ok = 1
    for c in s:
        d = ord(c) - 48
        if d not in (2, 3, 5, 7):
            ok = 0
            break
        tong += d
    kq.append("Yes" if ok and nt(n) and nt(int(s[::-1])) and nt(tong) else "No")
print('\n'.join(kq))