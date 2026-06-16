import math
from itertools import permutations

t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    for i in range(n):
        s.append(str(n-i))
    ds = permutations(s)
    print(math.factorial(len(s)))
    for c in ds:
        print("".join(c), end = " ")
    print("")