a = list(map(int, input().split()))
tong = sum(a)
if tong > 0:
    print("chiec giay con thieu ben trai size", tong, end="")
else:
    print("chiec giay con thieu ben phai size", -tong, end="")