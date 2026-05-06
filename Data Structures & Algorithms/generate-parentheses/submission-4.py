class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 백트래킹 + stack 조합 활용 
        result = []
        stack = []

        def dfs(opening, ending):
            # 완성조건 
            if opening == n and ending == n:
                result.append("".join(stack))
            
            if opening < n: 
                stack.append('(')
                dfs(opening+1, ending)
                stack.pop()

            if ending < opening: 
                stack.append(')')
                dfs(opening, ending+1)
                stack.pop()
            
        dfs(0,0)
        return result