class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        start, end = 0, len(s)-1

        while start < end: 
            if braces[s[start]] != s[end]:
                return False
            start += 1
            end -= 1

        return True