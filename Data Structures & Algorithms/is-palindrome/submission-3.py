import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        return ref == ref[::-1]
    