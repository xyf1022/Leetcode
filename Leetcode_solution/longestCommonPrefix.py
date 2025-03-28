# 题目：
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例：
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


solu = Solution()
print(solu.longestCommonPrefix(["fengchihua","fengruikun","fengyyu"]))