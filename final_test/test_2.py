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


if __name__ == '__main__':
    M = int(input())
    point_list = []
    distance_list = [[] for _ in range(M)]
    for _ in range(M):
        point = list(map(int, input().split(' ')))
        point_list.append(point)
    print(point_list)
    for i in range(len(point_list) - 1):
        for j in range(i, len(point_list)):
            distance = get_distance(point_list[i], point_list[j])
            distance_list[i].append(distance)
            if i != j:
                distance_list[j].append(distance)
    print(distance_list)




