class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^0-9A-Za-z]', '', s.lower())

        if s == s[::-1]: 
            return True 
        
        for i in range(len(s)):
            left_s = s[:i] + s[i+1:]
            if left_s == left_s[::-1]:
                return True
        
        return False
