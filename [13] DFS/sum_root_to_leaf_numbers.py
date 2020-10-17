# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Question: https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Solution: we DFS through the entire tree (any order works, we do postorder).

# We visit a node by computing the current sum at that node (equal to 10*previous sum + curnode.value),
# and "adding" the sum to the global sum IF the node is a leaf. 
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return sumNodes(root, 0)

def sumNodes(curNode, curSum):
    if curNode is None:
        return 0
    
    curSum = curSum*10 + curNode.val
    if curNode.left is None and curNode.right is None:
        return curSum
    
    return sumNodes(curNode.left, curSum) + sumNodes(curNode.right, curSum)
    
        