# input:
# 1
# 1 1,2 2,3 3,4 4,5 5,1.5 1.5

# output:
# 1 1,1.5 1.5,1.5 1.5,2 2

import sys


# 计算距离
def cal_dist(p1, p2):
    return (float(p1[0]) - float(p2[0])) ** 2 + (float(p1[1]) - float(p2[1])) ** 2


# 这里就是并归排序,只是排序的依据是点y值得大小
# 这里排序要改变原始数组arr的值,后续代码中要用到arr
def sort_y(l, r, arr):
    res = []
    mid = (l + r) >> 1
    i, j = l, mid + 1
    while i <= mid and j <= r:
        if arr[i][1] < arr[j][1]:  # 比较y值大小
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    while i <= mid:
        res.append(arr[i])
        i += 1
    while j <= r:
        res.append(arr[j])
        j += 1
    for i in range(0, r + 1 - l):
        arr[l + i] = res[i]


#
def merge(l, r, arr):
    if l == r:
        return sys.maxsize  # 如果是一个点则返回最大值
    if l + 1 == r:
        sort_y(l, r, arr)  # 两个点这里要并归一次
        return cal_dist(arr[l], arr[r])  # 返回距离
    mid = (l + r) >> 1
    d1 = merge(l, mid, arr)
    d2 = merge(mid + 1, r, arr)
    d = min(d1, d2)  # 更新左右距离中较小的
    sort_y(l, r, arr)  # 这里之后的arr[l,r]是按照y排序的了
    temp = []
    for i in range(l, r + 1):
        if abs(arr[i][0] - arr[mid][0]) <= d:
            temp.append(i)  # 寻找距离小于d的点
    #
    # temp.sort(key=lambda x: arr[x][1])  # 按照纵坐标排序
    # 求出temp中最近的一对点
    for i in range(len(temp)): # 所以这里的temp是已经按照y排过序的了
        for j in range(i + 1, len(temp)):
            if arr[temp[i]][1] - arr[temp[j]][1] > d:  # 如果纵坐标之差大于了目标距离,那就不用算了
                continue
            if j > i + 1 + 6:  # 如果大于6个点就停止
                break
            d3 = cal_dist(arr[temp[i]], arr[temp[j]])  # 计算距离
            d = min(d, d3)  # 更新较小值
    return d


point_list = []
for _ in range(int(input())):
    point_list = list(map(lambda x: [float(x.split(" ")[0]), float(x.split(" ")[1])], input().strip().split(",")))
point_list = sorted(point_list, key=lambda x: (x[0]))  # 先排序
ans = merge(0, len(point_list) - 1, point_list)
print_str = []
for i in range(len(point_list)):
    for j in range(i + 1, len(point_list)):
        if ans == cal_dist(point_list[i], point_list[j]):
            if int(point_list[i][0]) == point_list[i][0]:
                print_str.append('{0} '.format(int(point_list[i][0])))
            else:
                print_str.append('{0} '.format(point_list[i][0]))
            if int(point_list[i][1]) == point_list[i][1]:
                print_str.append('{0},'.format(int(point_list[i][1])))
            else:
                print_str.append('{0},'.format(point_list[i][1]))

            if int(point_list[j][0]) == point_list[j][0]:
                print_str.append('{0} '.format(int(point_list[j][0])))
            else:
                print_str.append('{0} '.format(point_list[j][0]))
            if int(point_list[j][1]) == point_list[j][1]:
                print_str.append('{0},'.format(int(point_list[j][1])))
            else:
                print_str.append('{0},'.format(point_list[j][1]))
print((''.join(print_str)[:-1]))