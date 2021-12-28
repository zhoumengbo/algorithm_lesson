# input:
# 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# output:
# 3 3 9 12 24 29 34 49 51 56 78 84 100

def count_sort(array):
    length = len(array)
    res = [None] * length
    # 首次循环遍历, 每个列表的数都统计
    for index in range(length):
        # p 表示 a[i] 大于列表其他数 的次数
        p = 0
        # q 表示 等于 a[i] 的次数
        q = 0
        # 二次循环遍历, 列表中的每个数都和首次循环的数比较
        for two_index in range(length):
            if array[index] > array[two_index]:
                p += 1
            elif array[index] == array[two_index]:
                q += 1
        for k in range(p, p + q):  # q表示相等的次数,就表示, 从p开始索引后, 连续q次,都是同样的数
            res[k] = array[index]
    return res


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    num_list.pop(0)
    res = count_sort(num_list)
    print_str = []
    for i in range(len(res)):
        if i == len(res) - 1:
            print_str.append('{0}'.format(res[i]))
        else:
            print_str.append('{0} '.format(res[i]))
    print(''.join(print_str))
