import math
def snt(n):
    if n<=1: return False
    if n ==2 : return True
    if n %2 ==0: return False
    for i in range(3, int(n**0.5)+1):
        if n%i==0: return False
    return True
def uoc(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if n//i != i:
                res.append(n//i)
    return sorted(res)
def giaithua(n):
    return math.factorial(n)

n = int(input())
print(giaithua(n))
print("YES" if snt(n) else "NO")
print(",".join(map(str, uoc(n))))