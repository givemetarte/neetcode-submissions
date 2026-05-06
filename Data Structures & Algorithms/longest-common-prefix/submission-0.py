class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # set list length 
        list_num = len(strs)
        prefix = ""

        # get least length 
        least_length = 200
        for word in strs: 
            if least_length >= len(word):
                least_length = len(word)
        
        for i in range(least_length): 
            letters = [ word[i] for word in strs]
            no_duplicates = set(letters)

            if len(no_duplicates) == 1: 
                prefix += word[i]
            else: break
        
        return prefix

                

                

