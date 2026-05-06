import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # bruce force로 전체 경우의 수 만들기 
        # 하나씩 돌아가면서 parens 검증 
        all_combinations = itertools.product(['(',')'], repeat=2*n)
        answers = []
        
        for text in all_combinations: 
            stack = []
            is_valid = True
            
            for ch in text:
                if ch in '(': # opening
                    stack.append(ch)
                else: # closing
                    if not stack:
                        is_valid = False
                        break
                    stack.pop()
            
            if is_valid and not stack: 
                answers.append(''.join(text))
        
        return answers

            
