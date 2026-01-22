t = int(input())
for _ in range(t):
    s = input()
    A=0
    for c in s:
        A+=int(c)
    print("YES" if A%3==0 else "NO")