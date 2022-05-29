# 在体育比赛中，给定n个队的集合P，每两个队之间都进行一场比赛则称为一个循环赛。
# 这样的循环赛经常用于为随后的单淘汰或双淘汰赛建立参赛队的次序和它们的种子队。
# 请为n个队的集合P设计一种构建循环赛的有效算法，保证最短时间内完成循环赛（每一个队伍每一天只能参加一场比赛），假设n是2的幂。

# input:
# 第1行：n, 队伍数量
# 第2行：输入队伍数量是否为2的k次方

def solve_2_k(team_list, match):
    n = len(team_list)
    if n == 2:
        match[team_list[0]].append(team_list[1])
        match[team_list[1]].append(team_list[0])
        return team_list
    f = solve_2_k(team_list[:n // 2], match)
    t = solve_2_k(team_list[n // 2:], match)
    for j in range(len(t)):
        for k in range(len(f)):
            match[f[k]].append(t[(k + j) % len(t)])
            match[t[(k + j) % len(t)]].append(f[k])
    return f + t


def solve(team_list, match):
    n = len(team_list)
    pin = 1
    for i in range(n - 1):
        if i != 0:
            t = team_list[pin:]
            t = [t.pop()] + t
            team_list = team_list[:pin] + t
        front = team_list[:n // 2]
        tail = list(reversed(team_list[n // 2:]))
        for i in range(len(front)):
            match[front[i]].append(tail[i])
            match[tail[i]].append(front[i])


if __name__ == "__main__":
    n = int(input())
    team_list = list(range(n))
    match = []
    for i in range(n):
        match.append([])
    is2_k = input("队伍的数量是否为2^k个？(y/n)：")
    if is2_k == 'y':
        solve_2_k(team_list, match)
    else:
        if n % 2 == 1:
            match.append([])
            team_list.append(n)
            solve(team_list, match)
        else:
            solve(team_list, match)
    print("循环赛的有效算法:{0}".format(match))
