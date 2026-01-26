def solve():
    owners = ["A", "B", "C"]

    for owner in owners:
        A1 = (owner == "C")
        A2 = True

        B1 = (owner != "C")
        B2 = (owner == "A")
        C1 = (owner == "C")
        C2 = (B2 is False)

        okA = (A1 + A2 == 1)
        okB = (B1 + B2 == 1)
        okC = (C1 + C2 == 1)

        if okA and okB and okC:
            print(owner)
            return

solve()
