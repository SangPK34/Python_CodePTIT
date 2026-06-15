import math

a, b = map(int, input().split())
k = math.gcd(a,b)
tu = int(a/k)
mau = int(b/k)
print(f"{tu}/{mau}")