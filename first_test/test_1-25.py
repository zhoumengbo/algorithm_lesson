# input:
# 2
# 4
# 2 3 2 5
# 11
# 2 3 2 5 4 12 2 3 3 3 12

# output:
# 2 2 3 5
# 3 3 3 3 2 2 2 12 12 4 5


for _ in range(int(input())):
    num = list(map(int, input().split(' ')))[0]
    num_list = list(map(int, input().split(' ')))
    num_dict = {}
    for key in num_list:
        if num_dict.get(key, 0) == 0:
            num_dict[key] = 1
        else:
            num_dict[key] += 1
    num_dict = sorted(num_dict.items(), key=lambda kv: (kv[1], -kv[0]), reverse=True)
    print_str = []
    for key in num_dict:
        for i in range(key[1]):
            print_str.append('{0} '.format(key[0]))
    print((''.join(print_str)[:-1]))

