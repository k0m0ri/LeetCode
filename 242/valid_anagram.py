class Solution:
    # return true, t is an anagram of s
    # pre: s="anagram", t="nagram"
    # post: true
    def isAnagram(self, s, t):

        if not len(s) == len(t):
            return False

        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        for char in t:
            if char in map:
                map[char] -= 1
            else:
                return False

        for val in map.values:
            if not val == 0:
                return False

        return True
