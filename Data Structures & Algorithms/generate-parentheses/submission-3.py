class Solution:
    # time O(2^N) 
    # space O(N): stack 만큼 호출 
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def dfs(opening, ending):
            if opening == n and ending == n: 
                return result.append(''.join(stack))
            
            if opening < n: 
                stack.append('(')
                dfs(opening+1, ending)
                stack.pop()
            
            if ending < opening: 
                stack.append(')')
                dfs(opening, ending+1)
                stack.pop()

        dfs(0, 0)
        return result