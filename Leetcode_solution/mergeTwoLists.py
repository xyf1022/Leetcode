# 定义ListNode类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定义Solution类，包含合并两个已排序链表的函数


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        # 示例用法


# 创建链表1: 1 -> 2 -> 8 ->10
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(10)

# 创建链表2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 创建Solution对象并调用mergeTwoLists方法
solution = Solution()
merged_list = solution.mergeTwoLists(l1, l2)

# 打印合并后的链表
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
# 输出应为: 1 -> 1 -> 2 -> 3 -> 4 ->
# 注意：输出末尾的"->"是多余的，实际使用中可能需要处理这个细节