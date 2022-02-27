# input:
# 2
# ABCPQR
# ADGJPRT

# output:
# RQP
# JGDA

def solution(s):
    res_step = 0
    res_s = ""
    res_len = 0
    # 初始化
    init = [0] * 26
    for i in s:
        init[ord(i) - ord('A')] = 1
    for j in range(26):
        if init[j] == 1:
            temp_step = 1
            while temp_step < 26:
                temp_s = ""
                temp_len = 0
                temp = j
                while temp < 26:
                    if init[temp] == 1:
                        temp_len += 1
                        temp_s = chr(temp + ord('A')) + temp_s
                        temp += temp_step
                    else:
                        break
                if temp_len > res_len:
                    res_len = temp_len
                    res_s = temp_s
                    res_step = temp_step
                elif temp_len == res_len:
                    if temp_step < res_step:
                        res_s = temp_s
                        res_step = temp_step
                    elif temp_step == res_step and ord(temp_s[-1]) > ord(res_s[-1]):
                        res_s = temp_s
                temp_step += 1
    return res_s


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().strip()
        result = solution(s)
        print(result)


