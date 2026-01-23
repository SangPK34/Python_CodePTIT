fibo =[0]*93
fibo[1] = 1
fibo[2] = 1
for i in range(3,93):
    fibo[i] = fibo[i-1] + fibo[i-2]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        print(fibo[i], end = " ")
    print()