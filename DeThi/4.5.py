import json

with open("flights.json", "r") as f:
    data = json.load(f)
ds = data["flights"]
t = int(input())
for _ in range(t):
    y, cmd = input().split()
    a=[]
    for i in ds:
        if y==i["year"]:
            a.append(int(i["passengers"]))
    if len(a) ==0: print("INVALID")
    elif cmd == "min": print(min(a))
    elif cmd == "max": print(max(a))
    elif cmd == "sum": print(sum(a))
    elif cmd == "avg": print(f"{sum(a)/len(a):.5f}")
