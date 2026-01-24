n = int(input())
a = list(map(float, input().split()))
a.sort()
A = 0
cnt =0
for i in range(0, len(a)):
    if a[i] != max(a) and a[i] != min(a):
        A += a[i]
        cnt+=1
print(f"{A/cnt: .2f}")