class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode() # avoid edge cases
        currentP = dummy
        carry = 0 # cases where like 7+8=15 but we need to make space for the 1 itself as linked lists can't print it fully
        while l1 or l2 or carry: # remember to add carry so it's also until carry is null/0
            v1 = l1.val if l1 else 0 # value will be first item IF l1 exists else l1 is null/0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # we first need to get the carry out of val to find its position. like the 1's place/index position
            carry = val // 10
            val = val % 10
            currentP.next = ListNode(val)

            # updating pointers
            currentP = currentP.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next