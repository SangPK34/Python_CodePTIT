# class TS:
#     def __init__(self, ten, ns, d1, d2, d3):
#         self.ten = ten
#         self.ns = ns
#         self.d1 = d1
#         self.d2 = d2
#         self.d3 = d3
#         self.tong = d1+d2+d3
#
#     def __str__(self):
#         return f"{self.ten} {self.ns} {self.tong:.1f}"
# ds = []
# ten = input()
# ns = input()
# d1 = float(input())
# d2 = float(input())
# d3 = float(input())
# ds.append(TS(ten, ns, d1, d2, d3))
# for ts in ds:
#     print(ts)

ten = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
print(ten+" " + ns + " " + f"{d1+d2+d3:.1f}")