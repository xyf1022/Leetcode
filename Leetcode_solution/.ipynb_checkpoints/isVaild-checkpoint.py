class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in dic:  # 当前字符是闭合括号
                if not stack or stack[-1] != dic[i]:  # 栈为空或栈顶元素不匹配 ,stack[-1]: 查看栈顶元素
                    return False
                stack.pop()  # 匹配成功，弹出栈顶元素
            else:
                stack.append(i)  # 不是闭合括号，压入栈中
        return not stack  # 栈为空时表示所有括号都正确匹配


sol = Solution()
print(sol.isValid("{()}"))  # 应该输出 True


sol = Solution()
print(sol.isValid("]"))  # 应该输出 True

