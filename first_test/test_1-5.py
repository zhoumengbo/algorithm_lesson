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


