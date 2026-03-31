a = list(map(int, input().split()))
print(sum(
    (i==0 and a[i]>a[i+1]) or
    (i==len(a)-1 and a[i]>a[i-1]) or
    (0<i<len(a)-1 and a[i]>a[i-1] and a[i]>a[i+1])
    for i in range(len(a))
))