# input:
# 1
# 2
# 1 1
# 7 5

# output:
# 0

# Manhattan Distance = |x2-x1|+|y2-y1|
# Euclidean Distance = ((x2-x1)^2 + (y2-y1)^2)^0.5 where points are (x1,y1) and (x2,y2).

from itertools import combinations
import collections


def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def euclidean_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# 网上看的处理方式，不太理解
def solution(input_l, number):
    res = 0
    x_l = []
    y_l = []
    for p in range(number):
        x_l.append(input_l[p][0])
        y_l.append(input_l[p][1])
    # 统计横、纵坐标的值和出现的次数
    x = collections.Counter(x_l)
    y = collections.Counter(y_l)
    for m in x:
        res += (x[m] * (x[m] - 1)) // 2
    for n in y:
        res += (y[n] * (y[n] - 1)) // 2
    return res


if __name__ == '__main__':
    for _ in range(int(input())):
        pairs_num = 0
        point_num = int(input())
        point_list = []
        for i in range(point_num):
            num_list = list(map(int, input().split(' ')))
            point_list.append(num_list)
        # combinations_list = list(combinations(point_list, 2))
        # for key in combinations_list:
        #     if manhattan_distance(key[0], key[1]) == euclidean_distance(key[0], key[1]):
        #         pairs_num += 1
        # print(pairs_num)
        print(solution(point_list, point_num))