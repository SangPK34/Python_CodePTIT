import math
t = int(input())
for i in range(t):
    s = input()
    print("YES" if math.gcd(int(s), int(s[::-1])) ==1 else "NO")