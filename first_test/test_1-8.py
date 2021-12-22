# input:
# 3
# 3 2 4
# 10 9 6
# 450 768 517

# output:
# 1
# 4
# 34


if __name__ == '__main__':
    for _ in range(int(input())):
        num_list = list(map(int, input().split(' ')))
        print((num_list[0] ** num_list[1]) % num_list[2])
