s = input()
k = int(input())
ds = {}
for i in range(0, len(s)-1, 2):
    x = int(s[i:i+2])
    ds[x] = ds.get(x, 0) + 1
a = list(ds.items())
a.sort(key = lambda x: x[0])
find = False
for ke, va in a:
    if va >= k:
        find = True
        print(f"{ke} {va}")
if find == False:
    print("NOT FOUND")