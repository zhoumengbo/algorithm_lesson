# 假设在平面中给出n个点，并且希望这些点分成A和B两组，
# 使得A中的每一个点到A中另一个点都比到B中任意一个点近，反之亦然。
# 请描述一个有效的算法能够做到这种划分。

if __name__ == '__main__':
    key_list = [i + 1 for i in range(5)]
    side_dict = {}.fromkeys(key_list, [])
    print(side_dict)
    side_dict[2] = [1, 2, 3]
    print(side_dict)