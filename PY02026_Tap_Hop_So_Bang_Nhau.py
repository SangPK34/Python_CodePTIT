n, m = map(int, input().split())
a = sorted(set(map(int, input().split())))
b = sorted(set(map(int, input().split())))
print("YES" if a == b else "NO")

