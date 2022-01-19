# input:
# 1
# 3 3
# 1 10 12 20 22 30
# 5 15 25

# output:
# 5 16 27


for _ in range(int(input())):
    character_list = list(map(int, input().split(' ')))
    interval_list = list(map(int, input().split(' ')))
    input_list = list(map(int, input().split(' ')))
    n = interval_list[len(interval_list) - 1] + 1
    nums_list = [0]
    index = 0
    while index < len(interval_list):
        left = interval_list[index]
        right = interval_list[index + 1] + 1
        for key in range(left, right):
            nums_list.append(key)
        index += 2
    print_str = []
    for i in input_list:
        print_str.append('{0} '.format(nums_list[i]))
    result = ''.join(print_str)
    print(result[:-1])


