class Solution:
    def isValid(self, s: str) -> bool:
        # 순서를 고려한 자료구조: stack (선입후출)
        stack = []
        opening = '({['
        closing = ')}]'
        parens = dict(zip(opening, closing))

        for ch in s: 
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                if not stack or ch != parens[stack.pop()]:
                    return False 
        
        return not stack
    # time O(n): 문자열 수만큼 루프 순회 
    # space O(n): 최대 문자열 개수만큼 스택에 추가