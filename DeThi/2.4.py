from builtins import int

t = int(input())
for _ in range(t):
    s = input()
    ds = {}
    for c in s:
        ds[c] = ds.get(c, 0) + 1
    k = max(ds, key=ds.get)
    print(k)