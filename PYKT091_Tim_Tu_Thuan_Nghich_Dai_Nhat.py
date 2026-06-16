import sys
def tn(s):
    return s == s[::-1]
sys.stdin = open("VANBAN.in", "r")
ds = {}
m = 0
for line in sys.stdin:
    for x in line.split():
        ds[x] = ds.get(x, 0) + 1
        if tn(x):
            m = max(m, len(x))
for k, v in ds.items():
    if tn(k) and len(k) == m:
        print(k, v)