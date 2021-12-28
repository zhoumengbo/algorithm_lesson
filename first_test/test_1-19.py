# input:
# 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# output:
# 3 3 9 12 24 29 34 49 51 56 78 84 100


def get_index(nums, left, right):
    n = nums[left]
    i, j = left, right
    while True:
        while i < right and nums[i] <= n:
            i += 1
        while nums[j] > n:
            j -= 1
        if i >= j:
            break
        else:
            swap(nums, i, j)
    nums[left] = nums[j]
    nums[j] = n
    return j


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def quick_sort(nums, left, right):
    if left >= right:
        return
    p = get_index(nums, left, right)
    quick_sort(nums, left, p - 1)
    quick_sort(nums, p + 1, right)
    return nums


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    num = num_list.pop(0) - 1
    res = quick_sort(num_list, 0, num)
    print_str = []
    for i in range(len(res)):
        if i == len(res) - 1:
            print_str.append('{0}'.format(res[i]))
        else:
            print_str.append('{0} '.format(res[i]))
    print(''.join(print_str))
