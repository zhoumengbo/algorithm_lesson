# input:
# 2
# 5 3
# 0 0 2 1 1
# 7 23
# 10 2 3 4 5 7 8

# output:
# 0 0 1 2 $
# 2 3 8 10 $2 4 7 10 $3 5 7 8 $

from itertools import permutations

for _ in range(int(input())):
    character_list = list(map(int, input().split(' ')))
    num = character_list[0]
    k = character_list[1]
    num_list = list(map(int, input().split(' ')))
    num_list.sort()
    print_str = []
    num_set = []
    for key in range(num):
        num_set.append(key)
    choose_list = list(permutations(num_set, 4))
    for key in choose_list:
        num_sum = 0
        for i in key:
            num_sum += num_list[i]
        if num_sum == k:
            print_set = []
            for i in key:
                print_set.append(str(i))
            print_set.sort()
            index = print_set
            if index not in print_str:
                print_str.append(index)
    for i in range(len(print_str)):
        index = 0
        for j in print_str[i]:
            print_str[i][index] = num_list[int(j)]
            index += 1
    print_str_unique = []
    for key in print_str:
        if key not in print_str_unique:
            print_str_unique.append(key)
    print_line = []
    for key in print_str_unique:
        for i in key:
            print_line.append('{0} '.format(i))
        print_line.append('$')
    print(''.join(print_line))





