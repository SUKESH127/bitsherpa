class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # QUESTION: https://leetcode.com/problems/longest-common-prefix/
        
        # APPROACH: Essentially "brute force". We look at the first word, and consider every prefix of that word in increasing length until
        # we find that there is a prefix that doesn't match all the array. 
        
        # For this solution O(mn) worst case runtime, where m is the the number of letters
        # in the shortest word in the list, and n is the number of words in the word list.   
        
        # Example: ["flowers", "flow", "flight"] -> we first grab the first letter from "flowers", which is "f". We then check whether "f" is the
        # first letter in all the rest of the words. Since it is, we then check "fl" (first two letters of "flowers"). Since it matches everything, 
        # we try "flo" (first 3 letters of "flower"), and find it doesn't match "fli" in flight. Thus we return "fl"

        common = ""
        
        # edge cases - the list of strings is empty, or nonexistent
        if strs is None or len(strs) is 0:
            return common
        
        #iterate over the length over the first word: i goes from 1 up to len
        firstWord = strs[0]
        for i in range(1,1+len(firstWord)):
            
            #grab the first i letters of the first word (the prefix)
            lenIPrefix = firstWord[0:i]
            
            #generate a boolean list corresponding to strs where each element is true if the corresponding word does match the prefix
            matches = [True if curString[0:i] == lenIPrefix else False for curString in strs]
            
            #if all words match the prefix, we can update our common prefix return value
            if sum(matches) == len(strs):
                common = lenIPrefix
            else:
                break
        
        return common