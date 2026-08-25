# use two pointers to go through list with a N node gap, and keep a dummy node before the first node so we can later on return dummy.next (the linked list)
# reason why is that when R reaches null / end of the list, L will always be on the node we will remove / Nth node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy # remember, they start in the same place, but only left will move
        right = head

        # making gap of size n
        while n > 0 and right:
            right = right.next
            n -= 1

        # shifting both pointers
        while right:
            left = left.next
            right = right.next

        # deleting
        left.next = left.next.next # we skip the node we'll delete

        return dummy.next