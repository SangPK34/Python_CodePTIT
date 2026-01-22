def check(s):
    for i in range(0, len(s)-1):
        if ord(s[i]) == ord(s[i+1]) :
            return 0
        if ord(s[i]) > ord(s[i+1]):
            if i ==0:
                return 0
            else:
                for j in range(i, len(s)-1):
                    if ord(s[j]) <= ord(s[j+1]):
                        return 0
                return 1


t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")