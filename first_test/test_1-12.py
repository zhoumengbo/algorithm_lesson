# input:
# 2
# 5
# 1 2 10 5 5
# 4 5 12 9 12
# 7
# 13 28 29 14 40 17 3
# 107 95 111 105 70 127 74

# output:
# 3 5
# 7 40


if __name__ == '__main__':
    for _ in range(int(input())):
        num = list(map(int, input().split(' ')))[0]
        entry_time = list(map(int, input().split(' ')))
        exit_time = list(map(int, input().split(' ')))
        num_dict = {}
        max_time = max(max(entry_time), max(exit_time))
        for key in entry_time:
            if key in num_dict.keys():
                num_dict[key] += 1
            else:
                num_dict[key] = 1
        for key in exit_time:
            if key + 1 in num_dict.keys():
                num_dict[key + 1] += -1
            else:
                num_dict[key + 1] = -1
        current_num = 0
        for i in range(max_time + 2):
            if i in num_dict:
                current_num += num_dict[i]
            num_dict[i] = current_num
        for key, value in num_dict.items():
            if value == max(num_dict.values()):
                print(value, key)
                break


