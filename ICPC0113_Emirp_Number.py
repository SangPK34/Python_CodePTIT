def check(n):
    s = str(n)
    z = s[::-1]
    if s==z: return False
    return arr[int(s)] and arr[int(z)]

def sang(n):
    check = [True] * (n + 1)
    check[0] = check[1] = False
    for i in range(2, int(n**0.5)+1):
        if(check[i]):
            for j in range(i*i, n+1, i):
                check[j] = False
    return check
arr = sang(10**6)
snt = []
for i in range(len(arr)):
    if arr[i] == True:
        snt.append(i)
t = int(input())
for _ in range(t):
    res = []
    n = int(input())
    for x in snt:
        if x > n: break
        if check(x):
            if res.count(x) == 0:
                y = int(str(x)[::-1])
                if y < n and res.count(y) == 0:
                    res.append(x)
                    res.append(y)
    print(" ".join(map(str, res)))