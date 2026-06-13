def check(s):
    if len(s) %2 != 0: return False
    if len(s) < 3: return False
    if s[0] == s[2]: return False
    if len(set(s[1::2])) != 1: return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")