from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):  # 这里的index 相当于字典中的 key
            if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target- value], index]  #  records[target - value] 会返回之前那个匹配元素的索引， index 是当前元素的索引
            records[value] = index    # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []

# 创建Solution对象并调用mergeTwoLists方法
solution = Solution()
nums = [2, 7, 11, 15]
target = 26

# 调用 twoSum 函数
result = solution.twoSum(nums, target)

print(result)  # 输出: [2, 3]