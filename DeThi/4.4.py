class DB:
    def __init__(self, ten, diem, hso, goal):
        self.ten = ten
        self.diem = diem
        self.hso = hso
        self.goal = goal
    def __str__(self):
        return f"{self.ten} {self.diem} {self.hso} {self.goal}"
n = int(input())
ds = []
for i in range(n):
    ten = input()
    diem, hso, goal = map(int, input().split())
    ds.append(DB(ten, diem, hso, goal))
ds.sort(key = lambda x: (-x.diem, -x.hso, -x.goal))
for i in ds:
    print(i)
