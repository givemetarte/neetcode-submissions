class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        # 시작 braces만 담는 곳
        check = []

        for ch in s: 
            if ch in braces.keys():
                if braces[ch] not in check: 
                    return False 
                else:
                    check.pop()
            if ch in braces.values():
                check.append(ch)

        if not check: return True