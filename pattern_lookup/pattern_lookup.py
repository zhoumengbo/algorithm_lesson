import json
import os

# 算法思路：
# 指定子字符串长度，对字符串进行遍历，找出出现次数最多的该长度下的所有子字符串。
# 若结果只有一个即为最终答案，若大于一个，则通过结果数量预估最长子字符串长度，大多数情况下即可直接得到答案。
# 若结果小于一个，则通过二分查找方式递归查找。
#
# 时间复杂度：最好O(n), 最坏O(n*log(n))
# 空间复杂度：O(n)
# question12: w70P83eUXeKqTlKbQIP
# question13: 9Cmi7i2QkUa5TUKFfCIq
# question14: Ans8nx2VAmEo
# question15: I6CsFTVqT3HpNIcpC3

min_length = 6
testcase_folder_path = "D:\\study\\算法练习\\pattern_lookup\\testcases"
question_folder_path = "D:\\study\\算法练习\\pattern_lookup\\questions"


def check_testcase():
    for root, dirs, files in os.walk(''r'' + testcase_folder_path):
        for file in files:
            testcase_path = testcase_folder_path + '\\' + file
            json_file = open(testcase_path, encoding='utf-8')
            for line in json_file:
                json_dict = json.loads(line)
                content = json_dict.get("content", None)
                answer = json_dict.get("answer", None)
                # check correctness
                print(testcase_path + "  answer: " + answer)
                pattern_lookup(content)
            json_file.close()


def resolve_question():
    for root, dirs, files in os.walk(''r'' + question_folder_path):
        for file in files:
            question_path = question_folder_path + '\\' + file
            json_file = open(question_path, encoding='utf-8')
            for line in json_file:
                json_dict = json.loads(line)
                content = json_dict.get("content", None)
                # get question result
                print(question_path)
                pattern_lookup(content)
            json_file.close()


def pattern_lookup(content):
    content_length = len(content)
    substring_length = 10  # 根据业务场景设置合适的初始值
    find_substring(content, content_length, substring_length)


def find_substring(content, content_length, substring_length):
    substring_dict = {}
    result = []
    for i in range(content_length - substring_length + 1):
        substring = content[i:i + substring_length]
        substring_dict[substring] = substring_dict.get(substring, 0) + 1
    for key, value in substring_dict.items():
        if value == max(substring_dict.values()):
            result.append(key)
    result_length = len(result)
    if result_length == 1:
        print(result[0])
    elif result_length < 1:
        find_substring(content, content_length, (min_length + substring_length) / 2)
    else:
        find_substring(content, content_length, substring_length + result_length - 1)


if __name__ == '__main__':
    check_testcase()
    resolve_question()
