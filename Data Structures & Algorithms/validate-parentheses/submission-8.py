class Solution:
    def isValid(self, s: str) -> bool:
        # 순서를 고려한 자료구조: stack (선입후출)
        stack = []
        parens = {'{':'}','[':']','(':')'}

        for ch in s: 
            if ch in parens: # opening
                stack.append(ch)
            else: # closing
                if not stack or ch != parens[stack.pop()]:
                    return False 
        
        return not stack
