# input:
# 2
# THIS IS A TEST TEXT,TEST
# AABAACAADAABAABA,AABA

# output:
# 10
# 0 9 12


def search(text, tag):
    index_list = []
    length = len(tag)
    for i in range(len(text) - length + 1):
        if text[i: i + length] == tag:
            index_list.append('{0} '.format(i))
    return ''.join(index_list)


if __name__ == '__main__':
    for _ in range(int(input())):
        input_list = list(map(str, input().split(",")))
        print(search(input_list[0], input_list[1])[:-1])