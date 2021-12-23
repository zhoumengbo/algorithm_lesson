# input:
# 2
# 7
# 7 6 5 4 3 2 1
# 6
# 5 6 4 9 2 1

# output:
# 7
# 5 6
# 1 2 3 4
# 5
# 4 6
# 1 2 9


# if __name__ == '__main__':
#     for _ in range(int(input())):
#         num = list(map(int, input().split(' ')))[0]
#         num_list = list(map(int, input().split(' ')))
#         i = 0
#         index = 0
#         while 2**i < num:
#             nums = []
#             for j in range(2**i):
#                 nums.append(num_list[index])
#                 index += 1
#                 if index == num:
#                     break
#             nums.sort()
#             print_str = []
#             for k in nums:
#                 if k == nums[len(nums) - 1]:
#                     print_str.append('{0}'.format(k))
#                 else:
#                     print_str.append('{0} '.format(k))
#             print(''.join(print_str))
#             # i += 1

if __name__ == '__main__':
    for _ in range(int(input())):
        num = list(map(int, input().split(' ')))[0]
        num_list = list(map(int, input().split(' ')))
        level = 0
        i = 0
        while i < num:
            cnt = int(pow(2, level))
            cnt -= 1
            j = min(i + cnt, num - 1)
            num_list = num_list[:i] + sorted(num_list[i:j + 1]) + num_list[j + 1:]
            str1 = ''
            new = []
            while i <= j:
                new.append(num_list[i])
                i += 1
            news_list = []
            for d in new:
                if d not in news_list:
                    news_list.append(d)
            for k in range(len(news_list)):
                if k == len(news_list) - 1:
                    print(news_list[k], end='\n')
                else:
                    print(news_list[k], end=' ')
            level += 1





