# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = l1 #pointer over l1
        j = l2 #pointer over l2
        
        # seed the new list w/ a dummy value
        newList = ListNode(-1)
        n = newList #pointer over the list to be returned
        
        #we basically perform the "merge" algorithm
        #from mergesort!
        while (i != None or j!= None):
            if i is None:
                n = addNode(n, j.val)
                j = j.next
            elif j is None:
                n = addNode(n, i.val)
                i = i.next
            elif i.val < j.val:
                n = addNode(n, i.val)
                i = i.next
            else:
                n = addNode(n, j.val)
                j = j.next
    
        returnPointer = newList.next
        newList.next = None
        return returnPointer

def addNode(n, val):
    newNode = ListNode(val)
    n.next = newNode
    n = n.next
    return n
            