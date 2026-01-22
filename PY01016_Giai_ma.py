t = int(input())
for T in range(t):
    s = input()
    for i in range(0, len(s), 2):
        for j in range(int(s[i+1])):
            print(s[i], end="")
    print("")
