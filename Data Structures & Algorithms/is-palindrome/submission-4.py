import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        start, end = 0, len(ref)-1

        while start < end:
            if ref[start] != ref[end]:
                return False
            start += 1
            end -= 1

        return True
    