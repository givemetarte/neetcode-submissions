class Solution:
    def isValid(self, s: str) -> bool:
        ls = s.split()
        opposed_ls = ls[::-1]
        return ls == opposed_ls