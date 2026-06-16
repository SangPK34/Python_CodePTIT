s = input()
ds = {}
for i in range(0, len(s)-1, 2):
    x = int(s[i:i+2])
    ds[x] = ds.get(x, 0) +1
for k, v in ds.items():
    print(k, v)