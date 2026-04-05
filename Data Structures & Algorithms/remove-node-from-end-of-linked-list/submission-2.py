# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next  ## [1 2 3 4] = 4

        removeIndex = N - n    ## 4 - 2
        if removeIndex == 0:
            return  head.next

        cur = head              # cur = 1
        for i in range(N - 1):     #  4 - 1
            if (i  + 1) == removeIndex:  # 0 + 1 ==! 2 skip 1 + 1 == 2 [1 , 2, 4]
                cur.next = cur.next.next
                break
            cur = cur.next
        return head     ### [1, 2, 4]