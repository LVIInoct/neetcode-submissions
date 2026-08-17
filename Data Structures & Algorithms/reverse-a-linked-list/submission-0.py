# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr is not None: # goes through the list
            nextNode = curr.next # store next
            curr.next = prev # reverse current node's next pointer
            # moving pointers
            prev = curr
            curr = nextNode
        return prev


