# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Question: https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Solution 1: We use a list as a parameter to keep track of the running
# sum of root-to-leaf sums (ie a global variable). After setting up the list,
# we start a post-order tree traversal (depth first search) to go through the tree.
# we use another float parameter to keep track of the sum at any node. 
# whenever we are at a leaf node, we add the sum to our runningSum param.

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        runSum = [0]
        curSum = 0
        dfs(root, curSum, runSum)
        return runSum[0]

def dfs(node, curSum, runSum):
    if node is None:
        return
    
    curSum = curSum*10 + node.val
    if node.left is None and node.right is None:
        runSum[0] += curSum
    
    dfs(node.left, curSum, runSum)
    dfs(node.right, curSum, runSum)


# Solution 2: Same post-order traversal, but without using
# a global variable 
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
    
        