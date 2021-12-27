# input:
# 1
# 3
# 1 2 3 4 5 6 7 8 9

# output:
# 1 2 3 4 5 6 7 8 9


# 看不懂题
for _ in range(int(input())):
    num = list(map(int, input().split(' ')))[0]
    num_list = list(map(int, input().split(' ')))
    num_list.sort()
    for i in range(len(num_list)):
        num_list[i] = '{0} '.format(num_list[i])
    print(''.join(num_list))
