t = int(input())
for _ in range(t):
    s = input()
    A= 1
    for c in s:
        if c!='0':
            A*= int(c)
    print(A)