class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding the middle
        slow, fast = head, head.next
        while fast and fast.next: # while it hasn't reached end or null
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #second half of list
        prev = slow.next = None # since post reordering itll be at the end

        # reversing second portion of the list using a prev pointer
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev # start at head. remembering that second is the second half of list
        while second: # second half may be shorter so we check if it's not null
            tmp1, tmp2 = first.next, second.next # saving next nodes before breaking link
            first.next = second # add second half node
            second.next = tmp1 # add first half node
            first, second = tmp1, tmp2 # update