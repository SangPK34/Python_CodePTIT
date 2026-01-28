while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    if a.count(a[0]) == n:
        print("BANG NHAU")
    else: print(str(min(a)) + " " + str(max(a)))
