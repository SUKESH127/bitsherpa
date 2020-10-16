# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution is pretty straightforward,
# explained here if needed - https://leetcode.com/problems/remove-duplicates-from-sorted-list/solution/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while (cur != None and cur.next != None):
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return head
            