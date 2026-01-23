while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0: break
    cnt = 0
    while not a == b == c == d:
        a1 = a
        b1 = b
        c1 = c
        d1 = d
        a = abs(a1 - b1)
        b = abs(b1 - c1)
        c = abs(c1 - d1)
        d = abs(d1 - a1)
        cnt += 1
    print(cnt)
