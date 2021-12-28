# input:
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# output:
# 3 3 9 12 24 29 34 49 51 56 78 84 100


def merge(seq, low, mid, high):
    left = seq[low: mid]
    right = seq[mid: high]
    k = 0
    j = 0
    result = []
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    result += left[k:]
    result += right[j:]
    seq[low: high] = result


def merge_sort(seq):
    i = 1
    while i < len(seq):
        low = 0
        while low < len(seq):
            # mid前后均为有序
            mid = low + i
            high = min(low + (2 * i), len(seq))
            if mid < high:
                merge(seq, low, mid, high)
            low += 2 * i
        i *= 2


num_list = list(map(int, input().split(' ')))
num = num_list.pop(0) - 1
merge_sort(num_list)
print_str = []
for i in range(len(num_list)):
    if i == len(num_list) - 1:
        print_str.append('{0}'.format(num_list[i]))
    else:
        print_str.append('{0} '.format(num_list[i]))
print(''.join(print_str))
