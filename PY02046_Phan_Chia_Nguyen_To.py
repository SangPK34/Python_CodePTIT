def snt(n):
    if n <=1: return False
    if n ==2: return True
    if n %2 ==0: return False
    for i in range(3, int(n**0.5)+1):
        if n % i ==0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
seen = set()
b = []
for x in a:
    if x not in seen:
        b.append(x)
        seen.add(x)

m = len(b)
find = False
kq = 10000
for i in range(len(b)):
    if snt(sum(b[:i+1])) and snt(sum(b[i+1:])):
        find = True
        kq = min(kq, i)
print(kq if find else "NOT FOUND")