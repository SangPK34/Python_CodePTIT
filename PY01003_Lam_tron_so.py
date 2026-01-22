from os.path import join

t = int(input().strip())
while (t>0):
    s = list(input().strip())
    n = len(s)
    for i in range(n-1, 0, -1):
        if s[i] >='5':
            s[i-1] = chr(ord(s[i-1])+1)
        s[i] = '0'
    if s[0] >'9':
        s[0] = '0'
        s.insert(0,'1')
    print("".join(s))
    t-=1