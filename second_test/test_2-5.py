# input:
# 2
# 2
# 1 2
# 4
# 0 10 20 30

# output:
# 1.50
# 3.82 15.00 26.18


for _ in range(int(input())):
    n = int(input())
    input_list = list(map(int, input().split(' ')))
    # 要求精度： 0.0000000000001
    precision = 0.00001  # 精度
    print_str = []
    for i in range(len(input_list) - 1):
        left = input_list[i]
        right = input_list[i + 1]
        while True:
            mid = (left + right) / 2
            f = sum(map(lambda x: 1 / (x - mid), input_list))
            if -precision < f < precision:
                print_str.append('{:.2f} '.format(mid))
                break
            elif f > precision:
                right = mid
            else:
                left = mid
    result = ''.join(print_str)
    print(result[:-1])
