# 一家专车公司每天必须处理客户的接送请求，将客户从他们的家（不同地方）接到当地机场。
# 假设现在有n个位置的接送请求，并且有n辆专车，其中第i辆车到位置j的距离dij是给定的。
# 请你描述一个派遣n辆专车到n个地点的有效算法，使得n个专车的总行程最小。

# 解决指派问题（匈牙利算法）
# input:
# 第1行：n, 车和地点数量
# 后面n行：第n辆车分别到各个地点的距离
# example:
# 4
# 1 3 5 7
# 2 4 6 8
# 5 4 3 5
# 3 6 7 10

import numpy as np
from scipy.optimize import linear_sum_assignment


if __name__ == "__main__":
    n = int(input())
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    cost = np.array(cost)
    row_index, col_index = linear_sum_assignment(cost)
    print(row_index)  # 开销矩阵对应的行索引
    print(col_index)  # 对应行索引的最优指派的列索引
    for i in row_index:
        print("第{0}辆车应该去第{1}个地点，距离为{2}".format(i, col_index[i], cost[i, col_index[i]]))
    print("最小总行程: {0}".format(cost[row_index, col_index].sum()))

