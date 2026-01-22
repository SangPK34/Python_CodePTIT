s = input()
hoa = sum(c.isupper() for c in s)
thuong = sum(c.islower() for c in s)
print(s.lower() if thuong>=hoa else s.upper())