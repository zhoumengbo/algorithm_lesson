# input:
# 1
# 7 a c,b c,c d,d e,d f,e g,f g

# output:
# 4


def input_pre():
    global name, pre, m, n
    for i in range(m):
        v = 0
        u = 0
        while u < n:
            if p[i][0] == name[u]:
                break
            else:
                u += 1
        if u == n:
            name.append(p[i][0])
            n += 1
        while v < n:
            if p[i][1] == name[v]:
                break
            else:
                v += 1
        if v == n:
            name.append(p[i][1])
            n += 1
        pre[v] |= (1 << u)


def solve():
    global dp, n
    dp[0] = 1
    for s in range(1 << n):
        if dp[s] != 0:
            for i in range(n):
                if ((s & pre[i]) == pre[i]) and not (s & (1 << i)):
                    dp[s | (1 << i)] += dp[s]
    print(dp[(1 << n) - 1])


for _ in range(int(input())):
    pairs = list(map(str, input()[2:].split(",")))  # 起点终点对集合
    m = len(pairs)
    n = 0
    p = []  # 存储起点终点对
    for i in range(m):
        pair = pairs[i].split()
        p.append(pair)
    name = []
    size = 13
    pre = [0 for i in range(size)]
    dp = [0 for i in range(1 << size)]
    input_pre()
    solve()

