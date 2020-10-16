# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # 1->2->3-NULL  ->  3-2-1-NULL
    # 1-NULL      ->  1-NULL
    
    # we just store the previous node
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while (cur != None):
            tmpNext = cur.next
            cur.next = prev
            prev = cur
            cur = tmpNext
        return prev
            
        