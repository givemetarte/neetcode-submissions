import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = re.sub(r"[a-z]","",s)
        start = 0
        end = len(ref)-1

        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True

    