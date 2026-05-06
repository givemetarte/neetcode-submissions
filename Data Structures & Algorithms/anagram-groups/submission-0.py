class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort 시켜서 맞는걸 판별 --> 해시테이블 사용 
        anagrams = {}

        for word in strs: 
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams: 
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())