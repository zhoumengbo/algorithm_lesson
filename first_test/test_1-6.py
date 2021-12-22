# input:
# 1
# 14

# output:
# 3


if __name__ == '__main__':
    for _ in range(int(input())):
        p_num = list(map(int, input().split(' ')))[0]
        kill_index = 1
        kill_p = 1
        while p_num >= kill_p:
            p_num -= kill_p
            kill_index += 1
            kill_p = kill_index * kill_index
        print(kill_index - 1)
