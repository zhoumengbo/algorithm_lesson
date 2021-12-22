# input:
# 1
# 4
# 12 34 67 90
# 2

# output:
# 113

# 与1-5一模一样，改下输入就可
def get_bucket_num(bucket_cap, book_list):
    bucket_sum = 0
    bucket_num = 1
    for board in book_list:
        bucket_sum += board
        if bucket_sum > bucket_cap:
            bucket_num += 1
            bucket_sum = board
    return bucket_num


def search(i, j, people_num, book_list):
    if i == j:
        print(i)
        return
    mid = (i + j) >> 1
    bucket_num = get_bucket_num(mid, book_list)
    if bucket_num <= people_num:
        search(i, mid, people_num, book_list)
    else:
        search(mid + 1, j, people_num, book_list)


if __name__ == '__main__':
    nums = int(input())
    for n in range(nums):
        N = int(input())
        book_list = list(map(int, input().split()))
        people_num = int(input())
        min_cap = max(book_list)
        max_cap = sum(book_list)
        search(min_cap, max_cap, people_num, book_list)
