from itertools import product
n = int(input())
for i in range(3, n+1):
    for p in product("ABC", repeat=i):
        s = "".join(p)
        if s.count("A") <= s.count("B") and s.count("B") <= s.count("C") and s.count("A")>0:
            print(s)