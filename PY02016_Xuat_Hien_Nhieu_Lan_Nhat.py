t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = dict()
    for x in a:
        mp[x] = mp.get(x,0)+1
    mps = dict(sorted(mp.items(), key=lambda x: (-x[1],x[0])))
    k = next(iter(mps))
    if mps[k] > n//2:
        print(k)
    else: print("NO")