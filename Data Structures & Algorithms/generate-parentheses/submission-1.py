class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(text, opening, ending):
            if opening == n and ending == n: 
                return result.append(text)
            if opening > n or opening < ending:
                return 
            dfs(text + '(', opening+1, ending)
            dfs(text + ')', opening, ending+1)


        dfs("",0,0)
        return result