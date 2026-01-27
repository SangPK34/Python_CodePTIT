from itertools import product

n = int(input())
res = []
for i in range(4, n+1):
    for p in product("2357", repeat=i):
        x = ''.join(p)
        set1 = set(x)
        if x[-1] != '2' and len(set1)>=4: res.append(x)
for x in res:
    print(x)
