import math

def snt(n):
    if(n<2): return 0
    if(n==2): return 1
    if(n%2==0): return 0
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0: return 0
    return 1

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    c  = math.gcd(int(a), int(b))
    A = sum(int(x) for x in str(c))
    print("YES" if snt(A) else "NO")
