n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(0, n-1):
    for j in range(i, n):
        if a[i] > a[j]:
            cnt+=1
print(cnt)
