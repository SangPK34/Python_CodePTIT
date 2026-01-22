t = int(input())
for i in range(t):
    n = int(input())
    A=0.0
    if n% 2 ==0:
        for i in range(2, n+1, 2):
            A += 1/i
    else:
        for i in range(1, n+1, 2):
            A += 1/i
    print(f"{A:.6f}")