class Solution:
    # return index of first non-repeating char
    # pre: s="leetcode"
    # post: 0
    def firstUnique(self, s):

        # corner case: len(s) == 1, return 0
        if len(s) == 1:
            return 0

        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        for i, char in enumerate(s):
            if map[char] == 1:
                return i
        return -1


solution = Solution()
print(solution.firstUnique("loveleetcode"))
