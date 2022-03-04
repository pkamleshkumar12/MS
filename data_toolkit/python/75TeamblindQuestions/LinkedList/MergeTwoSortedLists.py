"""
You are given the heads of two sorted linked list list1 and list2.
Merge the two lists in one sorted list. The list should be made by splicing
together the nodes of first two lists

Return the head of the merged linked list
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


if __name__ == '__main__':
    f_third = ListNode(0)
    f_second = ListNode(2, f_third)
    f_first = ListNode(1, f_second)

    s_third = ListNode(4)
    s_second = ListNode(3, s_third)
    s_first = ListNode(1, s_second)
    print(Solution().mergeTwoLists(f_first, s_first))
