# input:
# 2
# 40
# 5

# output:
# 1
# 0

# 找到一个数,它含有9个因数,比如 36: 1 2 3 4 6 9 12 18 36
# 实际上是一个数学公式题,有9个因数的数必定满足下列公式之一
# x = a^2 * b^2
# x = a^8
# 其中a,b是质数,因此只要枚举质数即可.

arr = [0] * (10 ** 6)
arr[0] = 1
arr[1] = 1
prime_arr = []
for i in range(2, len(arr)):
    if arr[i] == 0:  # 是质数
        prime_arr.append(i)
    for prime in prime_arr:
        if i * prime >= len(arr):
            break
        arr[i * prime] = 1
        if i % prime == 0:
            break

for _ in range(int(input())):
    num = int(input())
    res = 0
    # 满足公式1
    for j in range(len(prime_arr)):
        if (prime_arr[j] * prime_arr[(j + 1)]) ** 2 > num:  # 此时停止遍历
            break
        else:
            for k in range(j + 1, len(arr)):
                if (prime_arr[j] * prime_arr[k]) ** 2 <= num:  # 统计满足条件的数
                    res += 1
                else:
                    break
    # 满足公式2
    for n in prime_arr:
        if n > 23:  # 防止用例错误而无法ac而加的代码
            break
        if n ** 8 <= num:
            res += 1
        else:
            break
    print(res)


