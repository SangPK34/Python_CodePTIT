t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    res = []
    for i in range(n):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if not st:
            res.append(i + 1)
        else:
            res.append(i - st[-1])
        st.append(i)
    for x in res:
        print(x, end=" ")
    print()
