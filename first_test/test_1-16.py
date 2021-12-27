# input:
# 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# output:
# 3 3 9 12 24 29 34 49 51 56 78 84 100

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    num_list.pop(0)
    insertion_sort(num_list)
    print_str = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            print_str.append('{0}'.format(num_list[i]))
        else:
            print_str.append('{0} '.format(num_list[i]))
    print(''.join(print_str))
