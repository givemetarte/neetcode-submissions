class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 한글자 입력시 
        if len(s) <= 1: return True 

        # 문자열 정제 
        s = re.sub(r'[^0-9A-Za-z]', '', s.lower())
        start, end = 0, len(s)-1

        while start <= end: 
            if s[start] != s[end]:
                return False 
            else: 
                start += 1 
                end -= 1
        
        return True