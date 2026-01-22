t = int(input())
for c in range(t):
    s = input()
    if len(s)<4:
        print("NO")
        exit()
    print("YES" if s[:2] == s[-2:] else "NO")
