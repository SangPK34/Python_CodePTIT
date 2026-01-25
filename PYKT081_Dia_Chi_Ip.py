def check(s):
    a = s.strip().split(".")
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit(): return False
        if int(x) < 0 or int(x) > 255:
             return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")