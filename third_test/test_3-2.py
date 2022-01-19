# input:
# 1
# 1 2 3 4 5 6 7
# 3 5
# 2

# output:
# 4

for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    section_list = list(map(int, input().split(' ')))
    k = int(input())
    left = section_list[0]
    right = section_list[1]
    print(sorted(num_list[left-1:right])[k-1])

