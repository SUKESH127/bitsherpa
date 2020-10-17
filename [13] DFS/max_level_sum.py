# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Question: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Solution: We DFS through the tree starting from the root, visiting every node
# and keeping track of the levels of the nodes as a parameter in the DFS. We
# add the value of each node to a counter dictionary which keeps track of the
# sum of nodes visited per level. We then ultimately just return the level 
# with the maximal sum. 

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        # [1] We create an array of buckets (sums), where each
        # bucket will store the sum of nodes at each level
        # is sums[1] = sum at level1, sums[2] = sum at level2

        # We have to create an array of buckets rather than a dictionary
        # bc the prompt asks us to return the SMALLEST level X with a maximal sum.
        # if we just used a dictionary as our "counter", since dictionaries are unordered
        # we'd need to use some additional logic to figure out how to traverse the dictionary in
        # level sorted order

        # To create the array of buckets though, we need to know the maximum LEVEL of the tree,
        # in order to know how many buckets to make. Therefore we need to write a quick getDepth
        # method and perform a DFS in order to find the maximum level of the tree. 
        def getDepth(node):
            if node is None:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        sums = [0]*(getDepth(root)+1)
        
        # [2 Now we now "tally" up the sums by visiting all
        # the nodes in the tree using depth first search
        def dfs(node, level):
            #base case
            if node is None:
                return
            
            #visit current
            sums[level] += node.val
            
            #explore the rest
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        
        #[3] now that we have the sum at each level,
        #we just find the level w/ max sum
        maxS,maxI = -1,-1
        for i,val in enumerate(sums):
            if val > maxS:
                maxS = val
                maxI = i
                
        return maxI
        
        