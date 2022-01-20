class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        elif len(strs[0]) == 0:
            return strs[0]
            
        for i in range(len(strs[0])):
            if self.__is_same_prefix(strs[0][:i + 1], strs[1:]):
                prefix = strs[0][:i + 1]
                continue
            
            if i == 0:
                return ""
            else:
                break
        
        return prefix
    
    def __is_same_prefix(self, prefix, strs):
        for s in strs:
            if prefix not in s[:len(prefix)]:
                return False
        return True