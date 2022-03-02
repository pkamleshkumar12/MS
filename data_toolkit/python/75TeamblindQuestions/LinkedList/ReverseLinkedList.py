# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ITERATIVE SOLUTION
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


if __name__ == '__main__':
    third = ListNode(3)
    second = ListNode(2, third)
    first = ListNode(1, second)
    print(Solution().reverseList(first))
