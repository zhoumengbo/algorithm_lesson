# input:
# 1
# 4
# 12 34 67 90
# 2

# output:
# 113

def sum(arr, start, to):
    total = 0
    for i in range(start, to + 1):
        total += arr[i]
    return total


def find_max(arr, n, k):
    dp = [[0 for i in range(n + 1)]
          for j in range(k + 1)]
    for i in range(1, n + 1):
        dp[1][i] = sum(arr, 0, i - 1)
    for i in range(1, k + 1):
        dp[i][1] = arr[0]
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            best = 100000000
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p], sum(arr, p, j - 1)))
            dp[i][j] = best
    return dp[k][n]


a = int(input())
for i in range(a):
    input1 = list(map(int, input().split()))
    input2 = list(map(int, input().split()))
    input3 = list(map(int, input().split()))
    n = len(input2)
    k = input3[0]
    print(find_max(input2, n, k))
