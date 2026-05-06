class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s마다 순회하면서 가장 긴 palindrome 찾기 
        # 리스트에 palindrome 후보 저장 
        # 가장 length가 긴 palindrome 출력 

        palins = []

        for i in range(len(s)):
            for j in range(1,len(s)+1):
                text = s[i:j+1]
                reversed_text = text[::-1]
                if text == reversed_text:
                    palins.append(text)
        
        max, max_idx = 0, 0
        for i in range(len(palins)):
            if len(palins[i]) >= max: 
                max = len(palins[i])
                max_idx = i
        
        return palins[max_idx]



