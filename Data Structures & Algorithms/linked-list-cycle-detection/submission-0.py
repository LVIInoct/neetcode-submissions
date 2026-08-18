# Floyd turtle and hare thing
# If slow and fast meet then there's a loop as they can only meet in a cycle not a straight line
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
            