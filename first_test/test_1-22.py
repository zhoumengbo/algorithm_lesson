# input:
# 1
# 49 38 65 97 76 13 27 49 55 4
# 5 3

# output:
# 13 4 49 38 27 49 55 65 97 76


def shell_sort(num_list, index_list):
    new_index = []
    for i in index_list:
        new_index.append(num_list[i])
    new_index.sort()
    j = 0
    for i in index_list:
        num_list[i] = new_index[j]
        j += 1


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    gap_list = list(map(int, input().split(' ')))
    for gap in gap_list:
        for i in range(0, gap):
            index_list = []
            while i < len(num_list):
                index_list.append(i)
                i += gap
            shell_sort(num_list, index_list)
    print_str = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            print_str.append('{0}'.format(num_list[i]))
        else:
            print_str.append('{0} '.format(num_list[i]))
    print(''.join(print_str))

