import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = re.sub(r"[^a-zA-Z]","",s).lower()
        return ref == ref[::-1]
    