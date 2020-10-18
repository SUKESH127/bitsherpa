# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Solution 1: We use a list object as a parameter w/ global scope to keep track of the maxDepth.
# We instantiate this object in the main method, and then call a postOrder traversal that explores all
# the nodes in the trees, calculates the depth of each node, 

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxDepth = [-1] #list w/ a single item which stores the maxDepth 
        getDepths(root, maxDepth, 1) #this tree traversal will traverse the tree and update maxDepth
        return maxDepth[0] 

 
# this function just DFSs through the tree,
# computing the depth of each node and updating the
# max depth if necessary
# invariant: the curDepth parameter will always have the current depth of the node
def getDepths(node, maxDepth, curDepth):
    #base case
    if node is None:
        return
    
    #visit
    if curDepth > maxDepth[0]:
        maxDepth[0] = curDepth
    
    #explore children
    getDepths(node.left, maxDepth, curDepth + 1)
    getDepths(node.right, maxDepth, curDepth + 1)

        
# Solution 2: Using post-order traversal, but no global variable

# We use the recursive formulation that the "max depth" of any node
# is going to be 1 + the maxDepth of it's child node, for whichever
# of the two children has the greater depth. 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        maxLeftDepth = Solution.maxDepth(self,root.left)
        maxRightDepth = Solution.maxDepth(self,root.right)
        
        return 1 + max(maxLeftDepth, maxRightDepth)