def snt(n):
    if n <= 1: return 0
    if n == 2: return 1
    if n %2 ==0: return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return 0
    return 1

n = int(input())
a = list(map(int, input().split()))
ddau = []
nt = []
for i in range(n):
    if snt(a[i]):
        ddau.append(i)
        nt.append(a[i])
    else:
        ddau.append(-1)
nt.sort()
for i in range(n):
    if ddau[i] != -1:
        print(nt[0], end = " ")
        nt.pop(0)
    else:
        print(a[i], end = " ")