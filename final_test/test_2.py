# 假设在平面中给出n个点，并且希望这些点分成A和B两组，
# 使得A中的每一个点到A中另一个点都比到B中任意一个点近，反之亦然。
# 请描述一个有效的算法能够做到这种划分。

# input:
# 第1行：M, 平面中的点的数量
# 后面M行：x y, 分别是点的横纵坐标
# example:
# 5
# 1 1
# 1 3
# 3 4
# 4 4
# 2 2

import math


def get_distance(point1, point2):
    return math.sqrt(math.pow((point2[0] - point1[0]), 2) + math.pow((point2[1] - point1[1]), 2))


def addPoint(group_A, group_B, point_list, distance_list, order_list):
    order_set = {key: distance_list[0][key] for key in order_list}
    order_set = sorted(order_set.items(), key=lambda x: x[1], reverse=False)
    order_list = [order_set[key][0] for key in range(len(order_list))]
    for index in order_list:  # 依据对初始点距离长度从小到大进行遍历
        min_A, min_B = 99999, 99999
        for point_index in group_A:
            dis = distance_list[index][point_index]
            if dis < min_A:
                min_A = dis
        for point_index in group_B:
            dis = distance_list[index][point_index]
            if dis < min_B:
                min_B = dis
        if min_A < min_B:
            group_A.append(index)
        else:
            group_B.append(index)
    for index in range(len(group_A)):
        group_A[index] = point_list[group_A[index]]
    for index in range(len(group_B)):
        group_B[index] = point_list[group_B[index]]
    return group_A, group_B


if __name__ == '__main__':
    M = int(input())
    point_list = []
    distance_list = [[] for _ in range(M)]
    for _ in range(M):
        point = list(map(int, input().split(' ')))
        point_list.append(point)
    print("所有点集合: {0}".format(point_list))
    for i in range(len(point_list) - 1):
        for j in range(i, len(point_list)):
            distance = get_distance(point_list[i], point_list[j])
            distance_list[i].append(distance)
            if i != j:
                distance_list[j].append(distance)
    print("所有点之间的距离矩阵: {0}".format(distance_list))
    order_list = [key for key in range(M)]
    group_A = [0]
    max_point = distance_list.index(max(distance_list))
    group_B = [max_point]
    order_list.remove(0)
    order_list.remove(max_point)
    group_A, group_B = addPoint(group_A, group_B, point_list, distance_list, order_list)
    print("group_A: {0}".format(group_A))
    print("group_B: {0}".format(group_B))
