# input:
# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0

# output:
# a b c d


for _ in range(int(input())):
    character_list = list(map(str, input().split(' ')))
    node_list = list(map(str, input().split(' ')))
    node_num = character_list[0]
    node_first = character_list[1]
    pic_list = []
    for i in range(int(node_num)):
        lines_list = list(map(str, input().split(' ')))
        pic_list.append(lines_list)
    print_list = [node_first + ' ']
    next_node_list = [node_first]
    while len(print_list) < int(node_num):
        node_first = next_node_list.pop(0)
        for key in pic_list:
            if key[0] == node_first:
                for i in range(1, len(key)):
                    if key[i] == '1':
                        next_node_list.append(pic_list[i-1][0])
                        if (pic_list[i-1][0] + ' ') not in print_list:
                            print_list.append(pic_list[i-1][0] + ' ')
    result = ''.join(print_list)
    print(result[:-1])







