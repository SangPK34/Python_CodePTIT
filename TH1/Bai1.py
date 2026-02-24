Tong = float(input())
A = float(input())
R = float(input())
factor = 2 if A >= 0.1*Tong else 3
kq = (Tong - A)*R + A*(factor*R)
print(kq)