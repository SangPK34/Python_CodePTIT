def sang(n):
    check = [True] *(n+1)
    check[0] = check[1] = False
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i, n+1, i):
                check[j] = False
    return check
check = sang(10**6)
snt =[]
for i in range(len(check)):
    if check[i]==True:
        snt.append(i)

n, x =  map(int, input().split())
cnt = 0
print(x, end = " ")
for i in snt:
    if cnt == n:
        break
    x += i
    print(x, end= " " )
    cnt += 1
