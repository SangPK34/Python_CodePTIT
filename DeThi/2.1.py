t = int(input())
for _ in range(t):
    arr = input().split()
    s= arr[0]
    n = int(arr[1])
    kq = ""
    for c in s:
        if 'a'<= c <='z': kq += chr((ord(c) - ord('a')+n)%26 + ord('a'))
        elif 'A' <= c <= 'Z': kq += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    print(kq)