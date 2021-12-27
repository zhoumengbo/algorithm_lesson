# input:
# 2
# 4
# 4 3 2 1
# 5
# 1 5 4 3 2

# output:
# 2
# 2

for _ in range(int(input())):
    num = list(map(int, input().split(' ')))[0]
    num_list = list(map(int, input().split(' ')))
    sort_list = num_list.copy()
    sort_list.sort()
    tran_num = 0
    for i in range(len(num_list)):
        if num_list[i] != sort_list[i]:
            index = sort_list.index(num_list[i])
            temp = num_list[i]
            num_list[i] = num_list[index]
            num_list[index] = temp
            tran_num += 1
    print(tran_num)
