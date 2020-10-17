# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Question: https://leetcode.com/problems/validate-binary-search-tree/

#Solution: We use the property that a tree is a BST if and only if
# the inorder traversal is sorted. If this isn't obvious to you, 
# do a few examples on scratch paper w/ made up trees to see this.

# We thus do an inorder traversal, and to keep it o(1) storage
# we only store the previous node, and then compare each node
# with the value of the previous one. 

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = [float('-inf')]
        return isValid(root, prev)

def isValid(curNode, prev):
    if curNode == None:
        return True
    
    if not isValid(curNode.left, prev):
        return False
    
    if curNode.val <= prev[0]:
        return False
    prev[0] = curNode.val
    
    if not isValid(curNode.right, prev):
        return False
    
    return True