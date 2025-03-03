class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# 创建Solution类的一个实例
solution = Solution()

# 调用isPalindrome方法并传入一个整数参数
# 例如，检查121是否是回文数
result = solution.isPalindrome(121)

# 打印结果
print(result)  # 输出: True

# 再尝试一个非回文数的例子
result = solution.isPalindrome(123)

# 打印结果
print(result)  # 输出: False
