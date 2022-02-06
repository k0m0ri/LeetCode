import sre_compile
from tkinter import SOLID


class Solution:
    # reverse chars in words without changing word's order
    # pre: s="God Ding"
    # post: s="doG gniD"
    def reverseWords(self, str):
        def reverse(chars, front, end):
            # testcase: chars="God Ding", front=0, end=2
            # testcase: chars="doG Ding", front=1, end=1
            # testcase: chars="doG Ding", front=4, end=7
            # testcase: chars="doG ginD", front=5, end=6
            # testcase: chars="doG gniD", front=6, end=5
            while front < end:
                tmp = chars[front]
                chars[front] = chars[end]
                chars[end] = tmp
                front += 1
                end -= 1

        if len(str) <= 1:
            return str

        front = 0
        end = 0
        chars = list(str)
        # testcase: chars=God Ding front=0, end=3
        while end < len(chars):
            if chars[end] == ' ':
                # testcase: chars="God Ding", front=0, end=3
                reverse(chars, front, end - 1)
                front = end + 1
                # testcase: chars="doG Ding", front=4, end=3
            if end == len(chars) - 1:
                # testcase: chars="doG Ding", front=4, end=7
                reverse(chars, front, end)
                # testcase: chars="doG gniD", front=4, end=7
            end += 1
        return ''.join(chars)


solution = Solution()
print(solution.reverseWords("God Ding"))
