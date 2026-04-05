# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _recursivecall(self, head, n):
        if not head:
           return None
        head.next = self._recursivecall(head.next, n)
        n[0] -= 1
        if n[0] == 0:
            return head.next
        return head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self._recursivecall(head, [n])