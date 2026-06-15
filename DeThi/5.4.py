def tinh(a, b):
    lai = 0.0
    if b <= 2:
        if a < 10**9: lai = 2.5
        elif a >= 3*10**9: lai = 2.8
        else: lai = 2.7
    elif b <= 6:
        if a < 10**9: lai = 3.9
        elif a >= 3*10**9: lai = 4.3
        else: lai = 4.1
    elif b <= 12:
        if a < 10**9: lai = 4.8
        elif a >= 3*10**9: lai = 5.0
        else: lai = 4.9
    elif b <= 36:
        if a < 10**9: lai = 4.8
        elif a >= 3*10**9: lai = 5.1
        else: lai = 5.0
    else:
        if a < 10**9: lai = 4.7
        elif a >= 3*10**9: lai = 5.0
        else: lai = 4.9
    return a*(lai/12/100)*b
tien  = float(input())
thang = float(input())
print(f"{tinh(tien, thang):.0f}")