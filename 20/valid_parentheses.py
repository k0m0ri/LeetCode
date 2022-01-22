class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = ["END"]

        for char in s:
            if char in parentheses_dict:
                stack.append(parentheses_dict[char])
            else:
                parenthesis = stack.pop()
                if not parenthesis == "END" and parenthesis == char:
                    continue
                else:
                    return False

        return len(stack) == 1
