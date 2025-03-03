import numpy as np


def fill_spiral_matrix(m,n):
    # 定义矩阵上下左右的边界
    up, down, left, right = 0, m - 1, 0, n - 1
    # 初始化结果数组
    ans = np.zeros((m, n), dtype=int)
    # 定义当前要填充的数字
    num = 1

    # 当还有未填充的行或列时继续循环
    while up <= down and left <= right:
        # 从左到右填充顶部行
        for i in range(left, right + 1):
            ans[up][i] = num
            num += 1
        up += 1
        # 从上到下填充右侧列（如果还有未填充的列）
        for i in range(up, down + 1):
            ans[i][right] = num
            num += 1
        right -= 1  # 右边界左移

        # 如果还有未填充的行（注意：在填充右侧列后可能已经没有未填充的行了）
        if up <= down:
            # 从右到左填充底部行（注意：这里是 right - 1 到 left，因为 right 已经被减 1 了）
            for i in range(right, left - 1, -1):
                ans[down][i] = num
                num += 1
            down -= 1  # 下边界上移

        # 如果还有未填充的列（注意：在填充底部行后可能已经没有未填充的列了）
        if left <= right:
            # 从下到上填充左侧列（注意：这里是 down - 1 到 up，因为 down 已经被减 1 了）
            for i in range(down, up - 1, -1):
                ans[i][left] = num
                num += 1
            left += 1  # 左边界右移

    return ans


# 示例：填充一个 5x5 的螺旋矩阵
m=8
n = 5
spiral_matrix = fill_spiral_matrix(m,n)
print(spiral_matrix)