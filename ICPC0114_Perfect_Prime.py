def snt(n):
    if n <=1: return False
    if n == 2: return True
    if n % 2 == 0 : return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def check(n):
    s = str(n)
    if snt(n) == False: return False
    if snt(int(s[::-1])) == False: return False
    A = 0
    for x in s:
        if snt(int(x)) == False: return False
        A += int(x)
    if snt(A) == False: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input().strip())
    print("Yes" if check(n) else "No")