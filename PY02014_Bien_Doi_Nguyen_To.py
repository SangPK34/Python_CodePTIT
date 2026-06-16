def snt(n):
    if n <=1: return False
    if n ==2: return True
    if n%2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i ==0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
kq = 0
for x in a:
    d = 0
    while True:
        if snt(x-d) or snt(x+d):
            kq = max(kq, d)
            break
        d+=1
print(kq)