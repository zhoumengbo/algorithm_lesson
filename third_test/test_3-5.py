# input:
# 4
# 17
# 43
# 15
# 16

# output:
# 17
# 34
# 51
# Not Possible

from itertools import permutations

for _ in range(int(input())):
    k = input()
    array = list(map(lambda x: x, k))
    list_combination = list(set(permutations(array)))
    max_num = 0
    for key in list_combination:
        num = int(''.join(key))
        if num % 17 == 0:
            max_num = max(max_num, num)
    if max_num == 0:
        print("Not Possible")
    else:
        print(max_num)

