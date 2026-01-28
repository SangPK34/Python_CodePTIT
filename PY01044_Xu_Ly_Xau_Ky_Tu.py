s1 = input().strip().lower()
s2 = input().strip().lower()
set1 = set(s1.split())
set2 = set(s2.split())
a = set1 | set2
b = set1 & set2
a = sorted(a)
b = sorted(b)
print(" ".join(a))
print(" ".join(b))


