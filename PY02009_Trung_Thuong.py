t = int(input())
for _ in range(t):
    n = int(input())
    mp = {}
    for i in range(n):
        x = int(input())
        mp[x] = mp.get(x,0)+1
    mpsort = dict(sorted(mp.items(), key=lambda x: (-x[1], x[0])))
    print(next(iter(mpsort)))
