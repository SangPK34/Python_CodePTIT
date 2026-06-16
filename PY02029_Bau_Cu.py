n, m = map(int, input().split())
a = list(map(int, input().split()))
ds = {}
for x in a:
    ds[x] = ds.get(x, 0)+1
find = False
m = max(ds.values())
a = sorted(ds.items(), key = lambda x: (-x[1]))
for k, v in a:
    if v<m:
        print(k)
        find = True
        break
if find == False:
    print("NONE")