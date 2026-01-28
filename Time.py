s = int(input())

ngay = s // 86400
s %= 86400
gio = s // 3600
s %= 3600
phut = s // 60
giay = s % 60

print(ngay, gio, phut, giay, sep = ":")
