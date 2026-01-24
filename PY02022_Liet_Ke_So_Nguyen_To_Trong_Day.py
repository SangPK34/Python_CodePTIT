def snt(n):
    if n <= 1: return 0
    if n == 2: return 1
    if n % 2 == 0: return 0
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return 0
    return 1


n = int(input())
a = list(map(int, input().split()))
mp = {}
for x in a:
    if snt(x):
        mp[x] = mp.get(x, 0) + 1
for k, v in mp.items():
    print(k, v)
