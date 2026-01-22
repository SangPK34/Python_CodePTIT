def snt(n):
    if n<=1: return 0
    if n==2: return 1
    if n%2 ==0: return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return 0
    return 1

def check(s):
    if not snt(len(s)): return 0
    cnt = 0
    for i in s:
        if snt(int(i)):
            cnt+=1
    if cnt<=len(s)-cnt:
        return 0
    return 1

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")
