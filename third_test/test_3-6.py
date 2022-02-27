# input:
# 2
# 2
# 4

# output:
# 2
# 5

def create_list():
    num_list = [1]
    sum_num = 1
    child_num = 0
    for i in range(20):
        temp = sum_num
        sum_num = sum_num * 2 - child_num
        child_num = sum_num - temp
        num_list.append(sum_num)
    return num_list


if __name__ == '__main__':
    num_list = create_list()
    for _ in range(int(input())):
        k = int(input())
        print(num_list[k-1])


