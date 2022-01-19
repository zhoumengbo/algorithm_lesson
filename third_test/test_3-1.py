# input:
# 1
# 1A2BD3G4H56JK
# 23EFG4I5J6K7

# output:
# 23G456K
# 23G45JK

def get_path(i, j, res, l):
    # dpp = np.array(dp) # 可以debug观察数组结构
    if dp[i][j] == 0:
        if res[::-1] != "":
            l.append(res[::-1])
        # print(res[::-1])
        return
    if dp[i - 1][j] == dp[i][j - 1]:
        if dp[i - 1][j] == dp[i][j - 1] == dp[i][j]:
            get_path(i - 1, j, res, l)
            get_path(i, j - 1, res, l)
        else:
            get_path(i - 1, j - 1, res + str(a[j - 1]), l)
    elif dp[i - 1][j] > dp[i][j - 1]:
        get_path(i - 1, j, res, l)
    else:
        get_path(i, j - 1, res, l)


case_num = [int(x) for x in input().strip().split(" ")][0]
for i in range(case_num):
    a = input().strip()
    b = input().strip()
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]  # b+1行 a+1列,初始化为0
    # 构建dp数组
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    l_arr = []
    # 递归寻找子序列
    get_path(len(b), len(a), "", l_arr)
    # 去重
    l_arr = list(set(l_arr))
    l_arr.sort()
    if len(l_arr) == 0:
        print()
    for x in l_arr:
        print(x)
