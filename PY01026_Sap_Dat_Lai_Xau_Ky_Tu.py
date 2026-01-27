
t = int(input())
for _ in range(t):
    print("Test " + str(_+1) + ": ", end = "")
    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    print("YES" if s1 == s2 else "NO")