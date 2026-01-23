def snt(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def check(s):
    if snt(int(s[:3])) and snt(int(s[-3:])): return True
    else : return False

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")