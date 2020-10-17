# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Question: https://leetcode.com/problems/range-sum-of-bst

# Solution: Basically, all we have to do is find all the nodes in the tree
# that are between L and R. Since it's a BST though, we can avoid visiting all of the nodes

#Basic solution - using a "global variable"
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        globalSum = [0] #this is a list with one element, which will store the total sum that we return
        dfs(root, globalSum, L, R)
        return globalSum[0]
    
def dfs(node, globalSum, L, R):
    if node is None:
        return
    
    # visit the current node - add the value to our sum if eligible
    if L <= node.val <= R:
        globalSum[0] += node.val
        
    # the if statements help us avoid unnecessary searching, bc
    # since this is a binary search tree, there is no point
    # searching left if our current node's value is already is less than L
    # and no point going right if the current value is greater than R
    if node.val >= L:
        dfs(node.left, globalSum, L, R)
    
    if node.val <= R: 
        dfs(node.right, globalSum, L, R)
    
#Solution 2: Using no global variable
#Slight modification - using no global variable, and doing just an in-order traversal,
#ie starting at the lowest node and stopping once we find a node with value greater than R.
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return traverse(root, L, R, 0)


def traverse(cur, L, R, value):
    if cur is None:
        return value
    
    value = traverse(cur.left, L, R, value)
    
    if cur.val >= L and cur.val <= R:
        value += cur.val
     
    if (cur.val <= R):
        value = traverse(cur.right, L, R, value)
    
    return value
        