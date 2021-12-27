# input:
# 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# output:
# 3 3 9 12 24 29 34 49 51 56 78 84 100

def count_sort(arr, max):
    output = [0 for i in range(max)]
    count = [0 for i in range(max)]
    ans = ["" for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


for _ in range(int(input())):
    num_list = list(map(int, input().split(' ')))
    count_sort(num_list, max(num_list))
    print_str = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            print_str.append('{0}'.format(num_list[i]))
        else:
            print_str.append('{0} '.format(num_list[i]))
    print(''.join(print_str))
