# input:
# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0

# output:
# 4

def dfs(graph, x, list):  # 递归实现图的深度优先遍历
    global max_deep
    k = 0  # 若结点的相邻结点都被遍历,i回到上一个结点
    deep = 1
    for y in graph[x]:  # 结点的相邻结点遍历
        k += 1
        if y not in list:  # 如果此节点未被遍历,则加入list
            deep = 1
            list.append(y)
            deep += dfs(graph, y, list)  # 递归,继续遍历
            if deep > max_deep:
                max_deep = deep
        else:
            if k == len(graph[x]):
                return deep
    return deep


for _ in range(int(input())):
    character_list = list(map(str, input().split(' ')))
    node_list = list(map(str, input().split(' ')))
    node_num = character_list[0]
    node_first = character_list[1]
    graph = {}
    for i in range(int(node_num)):
        lines_list = list(map(str, input().split(' ')))
        key = lines_list.pop(0)
        value = []
        for j in range(len(lines_list)):
            if lines_list[j] == '1':
                value.append(node_list[j])
        graph[key] = value
    node_list = [node_first]
    max_deep = 0
    dfs(graph, node_first, node_list)  # 遍历传参,存放图的字典graph,遍历的起始点'a',遍历返回的结果列表list
    print(max_deep)
