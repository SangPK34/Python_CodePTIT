from itertools import product

def run(n):
    cnt = 0
    for i in range(1, 10**6):
        for p in product("012", repeat=i):
            s = "".join(p)
            if s[0] != "0" and s.count("2") > len(s)//2:
                print(s, end=" ")
                cnt += 1
                if cnt == n: return

t = int(input())
for _ in range(t):
    n = int(input())
    run(n)
    print()