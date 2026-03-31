ds = list(map(int, input().split()))
for i in range(len(ds)):
    if ds[i] < 0:
        ds[i] = -1
    elif ds[i] > 0:
        ds[i] = 1
for d in ds:
    print(d, end=" ")