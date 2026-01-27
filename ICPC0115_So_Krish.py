import math

def check(n):
    s = str(n)
    A = 0
    for x in s:
        A += math.factorial(int(x))
    return A == n

t = int(input())
for _ in range(t):
    n = int(input())
    print("Yes" if check(n) else "No")