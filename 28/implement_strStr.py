
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif haystack == "":
            return -1

        gamma = 1
        delta = 1
        # deltaはneedleの最後の文字と同じ文字が左方向に何文字前に出現したか
        while(delta < len(needle) and needle[len(needle) - delta - 1] != needle[-1]):
            delta += 1

        # gammaはneedleの最後の文字と異なる文字が左方向に何文字前に出現したか
        while(gamma < len(needle) and needle[len(needle) - gamma - 1] == needle[-1]):
            gamma += 1

        i = 0
        while i <= len(haystack) - len(needle):
            if not needle[-1] == haystack[i + len(needle) - 1]:
                i += gamma
            else:
                j = len(needle) - 2
                while j >= 0 and needle[j] == haystack[i + j]:
                    j -= 1

                if j == -1:
                    return i
                i += delta
        return -1


solution = Solution()
haystack = "hfjhasjdhjkacll"
needle = "acll"
print(solution.strStr(haystack, needle))
