# 假设你有一只山羊和一只狼需要在一个有向图中从一个结点s到结点t。
# 为了避免狼吃掉山羊，它们所走的道路不能有公共边。
# 假定存在这样的路径，请你描述一个在G中找出两条不相交路径的多项式算法，以帮助狼和羊顺利从s到t。

# input:
# 第1行：M N, M是顶点的数量, N是边的数量
# 后面N行：a b, 分别是边的起点和终点的编号
# 最后1行：s t, 查询从结点s到结点t的两条不相交路径
# example:
# 4 4
# 1 2
# 1 3
# 2 4
# 3 4
# 1 4

def search(graph, s, t):  # 基于栈对图中指定节点进行搜索
    stack = [s]  # 建立栈
    data = []  # 记录已经遍历过的结点
    not_find = True
    while not_find:
        n = stack.pop()  # 取出栈中最后一个元素并删掉
        data.append(n)
        nodes = graph[n]
        for i in nodes[::-1]:  # 栈先进后出
            if i not in data:
                stack.append(i)
                if i == t:
                    not_find = False
                    break
    data.append(t)
    return data


if __name__ == '__main__':
    num_list = list(map(int, input().split(' ')))
    M = num_list[0]
    N = num_list[1]
    key_list = [i + 1 for i in range(M)]
    graph = {}.fromkeys(key_list, [])
    for _ in range(N):
        side = list(map(int, input().split(' ')))
        tmp_list = graph.get(side[0], None).copy()
        tmp_list.append(side[1])
        graph[side[0]] = tmp_list
    find_st = list(map(int, input().split(' ')))
    print("有向图中顶点的数量为{0}，边的数量为{1}".format(M, N))
    print("graph: {0}".format(graph))
    print("起点:{0}, 终点:{1}".format(find_st[0], find_st[1]))
    dfs_list1 = search(graph, find_st[0], find_st[1])
    print("第一次dfs结果: {0}".format(dfs_list1))
    for i in range(len(dfs_list1)-1):
        tmp_list = graph.get(dfs_list1[i], None).copy()
        tmp_list.remove(dfs_list1[i+1])
        graph[dfs_list1[i]] = tmp_list
    print("删除边后 graph: {0}".format(graph))
    dfs_list2 = search(graph, find_st[0], find_st[1])
    print("第二次dfs结果: {0}".format(dfs_list2))
    print("两条不想交路径为: {0}和{1}".format(dfs_list1, dfs_list2))
