from itertools import product
res = []
for i in range(1, 6):
    for p in product("02468", repeat=i):
        s = "".join(p)
        if s[0] != '0': res.append(int(s+s[::-1]))
res.sort()

t = int(input())
for _ in range(t):
    n = int(input())
    for x in res:
        if x>=n:
            print()
            break
        print(x, end = " ")
