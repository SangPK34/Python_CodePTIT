t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = dict()
    for x in a:
        mp[x] = mp.get(x, 0) + 1
    for k, v in mp.items():
        if v % 2 == 1:
            print(k)
