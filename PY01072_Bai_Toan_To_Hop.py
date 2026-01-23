from itertools import combinations
n, k = map(int, input().split())
a  = list(map(int, input().split()))
b = sorted(set(a))
for i in combinations(b, k):
    print(*i)