data = open("DATA.in").read().split()
n = int(data[0])
idx = 1
for _ in range(n):
    k = int(data[idx])
    s = data[idx+1]
    idx+=2
    x = int(s, 2)
    if k == 2:
        print(bin(x)[2:])
    elif k == 4:
        if x == 0:
            print(0)
        else:
            res = ""
            while x > 0:
                res = str(x % 4) + res
                x //= 4
            print(res)
    elif k == 8:
        print(oct(x)[2:])
    elif k == 16:
        print(hex(x)[2:].upper())