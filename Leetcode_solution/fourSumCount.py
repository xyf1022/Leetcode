class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1 #方括号 [] 用于字典的键访问和赋值操作

        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count


# 创建 Solution 类的实例
solution = Solution()

# 定义测试数据
nums1 = [1, 7, 3]
nums2 = [-2, 5, -3]
nums3 = [-1, 9, 2]
nums4 = [6, -5, 0, 7]

# 调用 fourSumCount 方法并打印结果
result = solution.fourSumCount(nums1, nums2, nums3, nums4)
print(f"结果是{result}")  # 输出结果