def tao():
    ds = []
    a = 1
    while a <= 10**18:
        b = a
        while b <= 10**18:
            c = b
            while c <= 10**18:
                ds.append(c)
                c *= 5
            b *= 3
        a *= 2
    ds = sorted(set(ds))
    return {x: i + 1 for i, x in enumerate(ds)}

vt = tao()
t = int(input())
for _ in range(t):
    n = int(input())
    print(vt[n] if n in vt else "Not in sequence")