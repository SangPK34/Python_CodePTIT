def tong(s):
    A = 0
    for i in s:
        A += int(i)
    return A % 10 == 0

def check(s):
    for i in range(1, len(s)):
        if(abs(ord(s[i]) - ord(s[i-1])) != 2):
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) and tong(s) else "NO")