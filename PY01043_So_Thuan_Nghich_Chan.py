def tn(s):
    if len(s) %2 != 0: return False
    z = s[::-1]
    for i in range(len(z)):
        if z[i] != s[i] or int(z[i]) %2 !=0: return False
    return True
from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, 4):
        for p in product("02468", repeat=i):
            s = "".join(p)+"".join(p)[::-1]
            if s[0] != '0' and int(s)<n and tn(s):
                print(s, end = " ")
    print()