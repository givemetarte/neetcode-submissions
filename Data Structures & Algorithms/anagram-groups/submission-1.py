from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs: 
            alpha = [0] * 26
            for ch in word: 
                alpha[ord(ch)-ord('a')] += 1
            
            anagrams[tuple(alpha)].append(word)
        
        return list(anagrams.values())

    # time O(n * wlogw) --> 이걸 더 줄여보자 
    # space O(n * w) 최악의 경우 가정하면 anagram n*w개임 