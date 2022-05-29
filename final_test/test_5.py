# 假设一棵根树T有n个结点，每一个结点v有权重w(v)。
# 对于T的结点的子集S，如果S中没有结点是S中任何其他结点的子结点或父结点，称S为T的独立集。
# 请设计一个求T的最大权独立集的有效算法（一组结点的权就是这些结点权重的总和）。

# input:
# init Tree数据结构

# 树结构
class Tree:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def solve(Node):
    if len(Node.children) == 0:
        return Node.weight, [Node.weight]
    solve_grandchildren_w = []
    solve_grandchildren_l = []
    solve_children_w = []
    solve_children_l = []

    for i in Node.children:
        for j in i.children:
            w = solve(j)[0]
            l = solve(j)[1]
            solve_grandchildren_w.append(w)
            solve_grandchildren_l.append(l)

    for i in Node.children:
        w = solve(i)[0]
        l = solve(i)[1]
        solve_children_w.append(w)
        solve_children_l.append(l)
    c1 = Node.weight + sum(solve_grandchildren_w)
    c2 = sum(solve_children_w)
    if c1 > c2:
        t = [Node.weight]
        for i in solve_grandchildren_l:
            t += i
        return c1, t
    else:
        t = []
        for i in solve_children_l:
            t += i
        return c2, t


if __name__ == '__main__':
    Node = Tree(2)
    Node.children = [Tree(7), Tree(8)]
    Node.children[0].children = [Tree(3), Tree(5)]
    Node.children[1].children = [Tree(1), Tree(4)]
    c2, t = solve(Node)
    print("c2:{0}".format(c2))
    print("t:{0}".format(t))
