def check(s):
    if len(s) % 2 ==0:
        for i in range(0, len(s)-2):
            if(s[i] != s[i+2]):
                return False
        return True
    else:
        return s == s[::-1]

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")