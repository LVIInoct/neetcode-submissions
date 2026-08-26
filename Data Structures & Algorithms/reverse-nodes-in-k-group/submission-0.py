# I am so tired
# separate into groups.
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reversing
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next # Storing first node
            groupPrev.next = kth # Putting Kth at beginning of groupNext
            groupPrev = tmp # Setting it as last node
        return dummy.next

    # Helper function. Go through K length of nodes and decrease K as we get closer to target
    def getKth (self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr