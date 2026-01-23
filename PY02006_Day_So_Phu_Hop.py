def check(a, b):
    for i in range(len(a)):
        if a[i]>b[i]: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    print("YES" if check(a,b) else "NO")