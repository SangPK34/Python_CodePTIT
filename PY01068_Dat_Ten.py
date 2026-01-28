from itertools import product, combinations

n, k = map(int, input().split())
set1 = set(list(map(str, input().split())))
set1 = sorted(list(set1))
for p in combinations(set1, k):
    s = " ".join(p)
    print(s)