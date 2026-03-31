a = []
while len(a) < 10:
    a += list(map(int, input().split()))
print(len(set(x % 42 for x in a)))