def snt(n):
    if n <= 1: return False
    if n == 2: return True
    if n%2 ==0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def check(s):
    if not snt(len(s)):
        return False
    cnt = 0
    for c in s:
        if snt(int(c)): cnt += 1
    if cnt <= len(s)-cnt: return False
    return True

t = int(input())
for _  in range(t):
    s = input()
    print("YES" if check(s) else "NO")