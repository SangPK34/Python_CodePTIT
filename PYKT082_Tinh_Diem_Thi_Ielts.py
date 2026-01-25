def diem(n):
    if n <= 2: return 1.0
    if n <= 4: return 2.5
    if n <= 6: return 3.0
    if n <= 9: return 3.5
    if n <= 12: return 4.0
    if n <= 15: return 4.5
    if n <= 19: return 5.0
    if n <= 22: return 5.5
    if n <= 26: return 6.0
    if n <= 29: return 6.5
    if n <= 32: return 7.0
    if n <= 34: return 7.5
    if n <= 36: return 8.0
    if n <= 38: return 8.5
    return 9.0


def tron(n):
    x = n * 4
    k = int(x)
    if k % 4 == 1:
        k += 1
    elif k % 4 == 3:
        k += 1
    return k / 4


t = int(input())
for _ in range(t):
    l, r, s, w = map(float, input().split())
    L = diem(l)
    R = diem(r)
    tb = (L + R + w + s) / 4
    print(tron(tb))
