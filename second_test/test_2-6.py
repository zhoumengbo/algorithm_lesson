# input:
# 1
# 11 4
# 2 1 2 5 7 1 9 3 6 8 8
# 2 1 8 3

# output:
# 2 2 1 1 8 8 3 5 6 7 9


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    print_str = []
    index = 0
    for key in B:
        while index < len(A):
            if key == A[index]:
                print_str.append('{0} '.format(A[index]))
                A.pop(index)
            else:
                index += 1
        index = 0
    A.sort()
    for key in A:
        print_str.append('{0} '.format(key))
    result = ''.join(print_str)
    print(result[:-1])

