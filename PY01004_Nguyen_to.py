def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def snt(n):
    if n <2: return 0
    if n==2: return 1
    if n%2==0: return 0
    for i in range(3,int(n**0.5)+1, 2):
        if n%i==0: return 0
    return 1

t = int(input())
while(t>0):
    N = int(input())
    cnt = 0
    for i in range(1, N):
        if gcd(i, N) == 1: cnt += 1
    if snt(cnt):
        print("YES")
    else:
        print("NO")
    t-=1