t = int(input())
for _ in range(t):
    n = int(input())
    print(1, end = "")
    cnt = 0
    while n%2==0 and n >0:
        n//=2
        cnt+=1
    if cnt>0:
        print(" * 2^" + str(cnt), end = "")
        cnt =0
    for i in range(3, int(n**0.5)+1, 2 ):
        while n%i==0 and n >0:
            n//=i
            cnt +=1
        if cnt>0:
            print(" * " + str(i) + "^" + str(cnt), end = "")
            cnt=0
    if n > 1:
        print(" * " + str(n) + "^1", end = "")
    print("")