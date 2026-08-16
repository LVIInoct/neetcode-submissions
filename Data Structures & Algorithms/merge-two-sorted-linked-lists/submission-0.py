# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        SLL = ListNode() #avoiding edge case of inserting
        tail = SLL

        while list1 and list2: #while they aren't null
            if list1.val < list2.val:
                tail.next = list1 # send it to output
                list1 = list1.next #update pointer
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # proceed after each condition
        if list1: # if it's non-null
            tail.next = list1
        elif list2: # if it's non-null
            tail.next = list2
        return SLL.next