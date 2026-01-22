a, k, n = map(int, input().split())
cnt = 0
r = a % k
b = (k - r) if r != 0 else k
for i in range(b, n - a + 1, k):
    cnt +=1
    print(i, end=" ")
if cnt ==0: print("-1")