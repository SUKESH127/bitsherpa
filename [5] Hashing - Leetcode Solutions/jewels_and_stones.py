#question: https://leetcode.com/problems/jewels-and-stones/

#approach: explained inline

#runtime: linear - o(m+n) time where m is length of J and 
#n is length of S
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # first create a hash-set of jewels,
        # so that it can then check whether each stone is a jewel
        # in constant time thanks to the hash-set
        # this takes O(len(J)) time
        jwls = {}
        for j in J:
            jwls[j] = 0
        
        # now, for every stone, we check if it is a jewel
        # this takes O(len(S)) time
        count = 0
        for stone in S:
            if stone in jwls:
                count += 1
        return count