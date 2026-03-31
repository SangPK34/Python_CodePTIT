def fib(a, b):
    f = [0, 1, 1]
    for i in range(3, b + 1):
        f.append(f[i - 1] + f[i - 2])
    return ' '.join(str(f[i]) for i in range(a, b + 1))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(fib(a, b))