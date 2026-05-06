class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 가지치기 생각 
        result = []

        def dfs(text, opening, ending):
            # 종료조건 추가 
            if opening == n and ending == n: 
                return result.append(text)
            if opening > n or opening < ending: 
                return 
            dfs(text + "(", opening+1, ending)
            dfs(text + ")", opening, ending+1)

        dfs('', 0, 0)
        return result