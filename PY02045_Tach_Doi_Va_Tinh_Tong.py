s = input()
while(len(s)>1):
    k = len(s) // 2
    s1 = s[:k]
    s2 = s[k:]
    s = str(int(s1) + int(s2))
    print(s)