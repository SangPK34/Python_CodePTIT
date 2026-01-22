t = int(input())
while t>0:
    n, x, m = map(float, input().split())
    cnt = 1
    while 1==1:
        n = n+n*x/100
        if(n>=m):
            break
        cnt += 1
    print(cnt)
    t-=1
