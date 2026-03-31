s = input()
mp = {}
for c in s:
    if c in "2357":
        mp[c] = mp.get(c, 0) + 1
for k, v in mp.items():
    print(f"{k} {v}")