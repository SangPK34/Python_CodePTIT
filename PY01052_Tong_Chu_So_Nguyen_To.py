def snt(n):
    if n<=1: return 0
    if n==2: return 1
    if n%2 ==0: return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return 0
    return 1

t = int(input())
for _ in range(t):
    s = input()
    A = 0
    for i in s:
        A+= int(i)
    print("YES" if snt(A) else "NO")