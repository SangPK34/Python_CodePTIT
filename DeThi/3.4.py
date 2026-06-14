t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if len(x) != len(y):
        print("INVALID")
        continue
    set1 = set(x)
    set2 = set(y)
    kq = len(set1 & set2) / len(set1 | set2)
    print(f"{kq:.5f}")