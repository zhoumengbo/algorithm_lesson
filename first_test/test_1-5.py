# input:
# 2
# 2 4
# 10 10 10 10
# 2 4
# 10 20 30 40

# output:
# 20
# 60

def get_bucket_num(bucket_cap, board_list):
    bucket_sum = 0
    bucket_num = 1
    for board in board_list:
        bucket_sum += board
        if bucket_sum > bucket_cap:
            bucket_num += 1
            bucket_sum = board
    return bucket_num


def search(i, j, worker_num, board_list):
    if i == j:
        print(i)
        return
    mid = (i + j) >> 1
    bucket_num = get_bucket_num(mid, board_list)
    if bucket_num <= worker_num:
        search(i, mid, worker_num, board_list)
    else:
        search(mid + 1, j, worker_num, board_list)
    

if __name__ == '__main__':
    for _ in range(int(input())):
        worker_num = list(map(int, input().split(' ')))[0]
        board_list = list(map(int, input().split(' ')))
        min_cap = max(board_list)
        max_cap = sum(board_list)
        search(min_cap, max_cap, worker_num, board_list)


# 李奇的，能ac
# def sum(arr, start, to):
#     total = 0
#     for i in range(start, to + 1):
#         total += arr[i]
#     return total
# def findMax(arr, n, k):
#     dp = [[0 for i in range(n + 1)]
#           for j in range(k + 1)]
#     for i in range(1, n + 1):
#         dp[1][i] = sum(arr, 0, i - 1)
#     for i in range(1, k + 1):
#         dp[i][1] = arr[0]
#     for i in range(2, k + 1):
#         for j in range(2, n + 1):
#             best = 100000000
#             for p in range(1, j + 1):
#                 best = min(best, max(dp[i - 1][p],sum(arr, p, j - 1)))
#             dp[i][j] = best
#     return dp[k][n]
# a = int(input())
# for i in range(a):
#     input1 = list(map(int, input().split()))
#     input2 = list(map(int, input().split()))
#     n = len(input2)
#     k = input1[0]
#     print(findMax(input2, n, k))


