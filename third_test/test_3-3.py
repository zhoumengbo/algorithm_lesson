# input:
# 1
# 3 4
# 1 0 1 1
# 1 1 1 1
# 1 1 1 0

# output:
# 6

if __name__ == '__main__':

    # read data
    case_num = [int(x) for x in input().split(" ")][0]  # 测试用例个数
    while case_num > 0:

        temp = [int(x) for x in input().split(" ")]
        m = temp[0]  # 矩阵长
        n = temp[1]  # 矩阵宽
        matrix = []  # 原始矩阵

        for i in range(m):
            row = [int(x) for x in input().split(" ")]
            matrix.append(row)
        h_arr = [[0] * n for _ in range(m)]
        h_arr[0] = matrix[0]  # 初始化竖直条(悬线)矩阵
        # print(h)

        # # 初始化竖直条(悬线)长度
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    h_arr[i][j] = h_arr[i - 1][j] + 1

        # 核心算法:
        ans = 0
        stack = []

        for i in range(m - 1, -1, -1):
            for j in range(n):
                cur = h_arr[i][j]
                if len(stack) == 0:
                    stack.append((cur, j))
                    # print(cur)
                else:
                    pre_j = None
                    while len(stack) != 0 and cur < stack[-1][0]:  # 如果当前值小于栈顶,就一直弹栈
                        # print("{}, {}, stack : {}".format(i, j, stack))
                        h, pre_j = stack.pop()
                        area = h * (j - pre_j)  # 每次弹栈后都计算面积
                        ans = max(ans, area)
                        # print("area :{}".format(area))
                    # 如果当前值大于栈顶,就加入到栈中
                    # 如果栈中没元素并且当前值不为0
                    if cur != 0:
                        # 注意pre_j和j的区别
                        if len(stack) == 0:  # 如果空栈了,则添加的是上一次弹栈的j值, 即: 沿用上一個彈出的位置。
                            stack.append((cur, pre_j))
                        elif cur > stack[-1][0]:
                            stack.append((cur, j))  # 如果没空栈,则添加的是这次的j值
                    else:
                        # 如果当前遇到了0,则要更新pre_j值,即:重置上一次的坐标
                        pre_j = j
                if j == n - 1:  # 最后一轮结束后若栈中有剩余
                    while len(stack) != 0:
                        h, pre_j = stack.pop()
                        area = h * (j + 1 - pre_j)  # 每次弹栈后都计算面积
                        ans = max(ans, area)
                        # print("final {}".format(area))
        print(ans)
        case_num -= 1
