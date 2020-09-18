class Solution:
    def reverseVowels(self, s: str) -> str:
        # QUESTION: https://leetcode.com/problems/reverse-vowels-of-a-string/
        
        # APPROACH: We are essentially going to use a two pointers approach - it will be very similar
        # to the partition algorithm of quicksort. 
        
        # Specifically, we maintain two pointers (i/j), one at the beginning and one 
        # at the end of the string. We increment i and decrement j until both i and j are pointing to vowels.
        # Once i and j both point to vowels, we swap the characters.
        # We repeat this process (of increment i/decrementing j until they're vowels + swapping) until the pointers cross
        
        
        
        #instantiate a set datatype, since we want to check if. Notice this is the set datatype!
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        #set up a list that we will iterate through, and our lower/upper pointers
        L = list(s)
        i = 0
        j = len(s) - 1
        
        while (i < j):
            # increment i until we are at a vowel
            while (L[i] not in vowels and i < j):
                i += 1
                
            # decrement j until we are at a vowel 
            while (L[j] not in vowels and i < j):
                j -=1
            
            #now swap i and j -> then increment i, decrement j so we can move on
            L[i],L[j] = L[j], L[i]
            i += 1
            j -=1
        
        return ''.join(L)
            