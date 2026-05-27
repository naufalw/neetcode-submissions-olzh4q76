class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mappings = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for i in s:
            if i in "({[":
                stack.append(mappings[i])
            else:
                if not stack or i != stack.pop():
                    return False
        
        return True if not stack else False


        