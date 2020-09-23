class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Solution is a classic easy problem - just not to swap
        #elements using two pointers until the pointers meet in the middle
        #i is the lower pointer, j is the upper pointer
        i = 0
        j = len(s) - 1
        
        while (i < j):
            s[i],s[j] = s[j], s[i] #cool functionality in python, can swap things on a single line like this rather than using a tmp variable
            i += 1
            j -= 1
        
        