t = int(input())
while(t>0):
    s = input()
    cnt =1
    res = ""
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            res+=str(cnt)+s[i]
            cnt=1
    res+=str(cnt)+s[-1]
    print(res)
    t-=1
