t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    set1 = set(a)
    l = min(set1)
    r = max(set1)
    print(r-l+1 - len(set1))
