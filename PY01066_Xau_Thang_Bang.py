def check(s):
    a = s[::-1]
    for i in range(0, len(s)-1):
        if abs(ord(a[i])-ord(a[i+1])) != abs(ord(s[i]) - ord(s[i+1])): return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")