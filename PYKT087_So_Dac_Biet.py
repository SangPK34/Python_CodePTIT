M = 10**9 + 7
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = bin(k)[:1:-1]
    kq = 0
    for i in range(len(s)):
        if s[i] == '1':
            kq += (pow(n, i, M)) % M
    print(kq%M)