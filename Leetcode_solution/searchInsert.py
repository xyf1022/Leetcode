from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left ,right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return right+1  # 如果循环结束还没有返回（即 target 不在数组中），则 left 会大于 right。
                        # 此时，right+1 就是 target 应该插入的位置，
                        # 因为 right 指向的是最后一个小于 target 的元素的索引（或者如果所有元素都大于 target，则指向 -1），
                        # 所以 right+1 正好是新元素的插入位置


solution = Solution()

# 定义输入参数
nums = [1, 3, 5, 6]
target = 5

# 调用 searchInsert 方法
result = solution.searchInsert(nums, target)

# 打印结果
print(result)  # 输出应该是 2，因为 5 在索引 2 处