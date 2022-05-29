# 假设给出电话网络图G，其顶点是交换中心，边表示两个交换中心之间的通信线路。
# 边的权重表示带宽大小。G中任意两个交换中心之间路径的带宽是路径上最低带宽。
# 请描述一个算法，用于计算任意两个交换中心a和b之间路径的最大带宽（从多个路径中选择一个最大的）。

# input:
# 第1行：n, 平面中的点的数量
# 第2行：s, t, 起点和终点
# 后面n行：每个点的到其他点的带宽大小
# example:
# 4
# 0 3
# -1 2 4 -1
# 2 -1 1 1
# 4 1 -1 3
# -1 1 3 -1

# 保存临时路径
path = []
# 保存包含最大权重边的路径
max_path = None
# 保存临时路径访问过的结点
visited = []
# 保存最大权重边
max_edge = None


# 深度优先遍历
def dfs(graph, s, t):
    # 找到一条路径则将里面的最小边与目前min_edge比较，如果过更小则更新最小边和包含它的路径
    if s == t:
        global max_edge
        global max_path
        if max_edge is None:
            max_edge = max(path)
            max_path = path.copy()
        else:
            temp = max(path)
            if temp > max_edge:
                max_path = path
                max_edge = temp
        return
    visited.append(s)
    for k in range(len(graph[s])):
        if graph[s][k] != 0 and k not in visited:
            path.append(k)
            dfs(graph, k, t)
            path.pop()
    return


if __name__ == '__main__':
    n = int(input())
    s, t = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    dfs(graph, s, t)
    print("{0}和{1}之间路径的最大带宽路径为：{2}".format(s, t, max_path))
