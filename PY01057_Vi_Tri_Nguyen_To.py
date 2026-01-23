def snt(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def check(s):
    for i in range(len(s)):
        if snt(i):
            if not snt(int(s[i])):
                return False
        else:
            if snt(int(s[i])):
                return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")