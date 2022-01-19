class Solution:    
    def romanToInt(self, s: str) -> int:
        dic_roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        pre_roman = ''
        
        for i in range(len(s) - 1, -1, -1):
            if ((s[i] == 'I' and (pre_roman == 'V' or pre_roman == 'X')) or
                (s[i] == 'X' and (pre_roman == 'L' or pre_roman == 'C')) or
                (s[i] == 'C' and (pre_roman == 'D' or pre_roman == 'M'))):
                ans -= dic_roman_to_integer[s[i]]
            else:
                ans += dic_roman_to_integer[s[i]]
            
            pre_roman = s[i]
            
        return ans