# input:
# 2
# 10
# 4 5 12
# 1 2 3
# 10 9 6
# 4 6 5
# 4 3 2
# 4 10 10
# 1 2 16
# 10 9 32
# 1 14 10
# 10 10 4
# 2
# 20 3 4
# 20 3 4

# output:
# 1 14 10
# 1 2 3
# 1 2 16
# 4 10 10
# 4 6 5
# 4 5 12
# 4 3 2
# 10 10 4
# 10 9 6
# 10 9 32
# 20 3 4
# 20 3 4


if __name__ == '__main__':
    for _ in range(int(input())):
        num = list(map(int, input().split(' ')))[0]
        i = 1
        nums_list = []
        while i <= num:
            num_list = list(map(int, input().split(' ')))
            num_list[1] = 1000 - num_list[1]
            nums_list.append(num_list)
            i += 1
        nums_list.sort()
        for sorted_list in nums_list:
            sorted_list[1] = 1000 - sorted_list[1]
        for score_list in nums_list:
            score_str = []
            for score_index in range(len(score_list)):
                if score_index == len(score_list) - 1:
                    score_str.append(str(score_list[score_index]))
                else:
                    score_str.append('{0} '.format(score_list[score_index]))
            print(''.join(score_str))

