from functools import lru_cache
class Solution: 
    # The recursive formulation here is that for any string,
    # wordBreak returns TRUE if the following the following conditions are
    # met for ANY prefix/suffix split of the word:
    # [1] The prefix is in the dictionary
    # [2] wordBreak(suffix) is also TRUE
    # The base case is when the argument string is itself in the dictionary
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # note: I am employing a fun trick here of using an inner function
        # you don't really need to do/use this, but it's just saves a 
        # tiny amount of time because because you don't have to pass 
        # the arguments from your driver function to your recursive function - 
        # you can just use them directly. 
        # Specifically, an inner function has access to all the arguments of
        # the outer function which it is inside. 
        
        
        @lru_cache(None)
        def wordBreak2(s):
            #base case - the entire string is in the dictionary
            if s in wordDict:
                return True

            # for each prefix/suffix split, we check if the prefix is
            # is in the dictionary, and if so, we check if wordBreak(suffix) is also TRUE
            # note: i goes from 1 to len(s) inclusive
            for i in range(1,len(s)+1):
                firstString = s[0:i]
                secondString = s[i:]
                if firstString in wordDict:
                    if wordBreak2(secondString):
                        return True
            return False
        
        return wordBreak2(s)