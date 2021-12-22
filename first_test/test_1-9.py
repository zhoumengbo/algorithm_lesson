# input:
# 2
# 3
# 1 2 3 1 5 6
# 3
# 1 2 4 4 5 1

# output:
# 1 2, 3 1, 5 6
# 1 2, 4 4, 5 1

# 凸包问题的分治解法 （来自https://blog.csdn.net/weixin_44851932/article/details/103152899）
def convex_problem(first, final, lis, result):
    maxDistance = 0
    index = -1
    # 处理上凸包
    if first < final:
        for i in range(first, final):
            firstPoint = lis[first]
            finalPoint = lis[final]
            first_x = firstPoint[0]
            first_y = firstPoint[1]
            final_x = finalPoint[0]
            final_y = finalPoint[1]
            indexPoint = lis[i]
            index_x = indexPoint[0]
            index_y = indexPoint[1]
            distance = first_x * final_y + index_x * first_y + final_x * index_y - index_x * final_y - final_x * first_y - first_x * index_y
            if distance > maxDistance:
                maxDistance = distance
                index = i
            if distance == 0:
                result[i] = 1
        # 处理下凸包
    else:
        for i in range(final, first):
            firstPoint = lis[first]
            finalPoint = lis[final]
            first_x = firstPoint[0]
            first_y = firstPoint[1]
            final_x = finalPoint[0]
            final_y = finalPoint[1]
            indexPoint = lis[i]
            index_x = indexPoint[0]
            index_y = indexPoint[1]
            distance = first_x * final_y + index_x * first_y + final_x * index_y - index_x * final_y - final_x * first_y - first_x * index_y
            if distance > maxDistance:
                maxDistance = distance
                index = i
            if distance == 0:
                result[i] = 1
    if index != -1:
        result[index] = 1
        convex_problem(first, index, lis, result)
        convex_problem(index, final, lis, result)


def isOnLine(first, final, index, lis):
    re = False
    firstPoint = lis[first]
    finalPoint = lis[final]
    indexPoint = lis[index]
    a = finalPoint[1] - firstPoint[1]
    b = firstPoint[0] - finalPoint[0]
    c = finalPoint[0] * firstPoint[1] - firstPoint[0] * finalPoint[1]
    judge = a * indexPoint[0] + b * indexPoint[1] + c
    if judge == 0:
        re = True
    return re


if __name__ == '__main__':
    nums = int(input())
    for T in range(nums):
        N = int(input())
        arr = list(map(int, input().split()))
        lis = []
        result = [0 for x in range(N)]  # 标记凸包点
        resultList = []
        k = 0
        for i in range(N):
            lis.append([arr[k], arr[k + 1]])
            k += 2
        lis.sort()   # 按横坐标排序
        isAllOnLine = True
        for i in range(N):
            if isOnLine(0, N-1, i, lis) is False:
                isAllOnLine = False
                break
        if isAllOnLine is True:
            for i in range(N):
                if i == 0 or i == N-1:
                    resultList.append(lis[i])
                else:
                    resultList.append(lis[i])
                    resultList.append(lis[i])
        else:
            if N <= 3:  # 如果点的数量小于等于3，则3个点均为凸包点
                for i in range(N):
                    result[i] = 1
            else:
                result[0] = 1  # x最大和最小的点肯定为凸包点
                result[N - 1] = 1
                convex_problem(0, N - 1, lis, result)   # 求上凸包
                convex_problem(N - 1, 0, lis, result)   # 求下凸包
            for i in range(len(result)):
                if result[i] == 1:
                    resultList.append(lis[i])
        for i in range(len(resultList) - 1):
            conpoint = resultList[i]
            print(conpoint[0], end=' ')
            print(conpoint[1], end=', ')
        conpoint = resultList[-1]
        print(conpoint[0], end=' ')
        print(conpoint[1])


