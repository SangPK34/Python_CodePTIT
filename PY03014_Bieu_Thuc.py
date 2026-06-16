n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    st = []
    res = []
    for c in s:
        if c == '(':
            cnt += 1
            st.append(cnt)
            res.append(cnt)
        elif c == ')':
            x = st.pop()
            res.append(x)
    print(*res)
