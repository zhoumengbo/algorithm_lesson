# input:
# 1
# 8
# 8 3 2 9 7 1 5 4

# output:
# 17


for _ in range(int(input())):
    num = list(map(int, input().split(' ')))[0]
    num_list = list(map(int, input().split(' ')))
    count = 0
    while len(num_list) > 0:
        max_index = num_list.index(max(num_list))
        max_count = len(num_list) - max_index - 1
        count += max_count
        num_list.pop(max_index)
    print(count)

