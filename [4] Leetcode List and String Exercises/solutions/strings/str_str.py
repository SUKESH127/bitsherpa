class Solution(object):
    def strStr(self, haystack, needle):
        # QUESTION: https://leetcode.com/problems/implement-strstr/
        
        # APPROACH: we iterate through all subsequences of length needle in haystack, 
        # until we find needle
        
        #start at index 0
        #end at index len(haystack) - len(needle)
        for i in range(len(haystack) -len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
            
        return -1
        