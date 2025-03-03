from sys import prefix


def kmp_search(string, pattern):
    next = build_next(pattern)

    i = 0
    j = 0
    while i < len(string) :
        if string[i] == pattern[i]:
            i += 1
            j += 1
        elif j > 0:
            j = next[j-1]
        else:
            i += 1

    if  j == len(pattern):
        return i - j

def build_next(pattern):
    """
    计算 Next 数组
    :param pattern:
    :return:
    """
    next = [0]  # next 数组 （初值元素为一个 0）
    prefix_len = 0  # 当前共同前后缀的长度
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            next.append(i)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i +=1
            else:
                prefix_len = next[prefix_len-1]
    return next

