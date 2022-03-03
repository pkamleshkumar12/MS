# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        turtle = head.next
        hare = head.next.next
        while turtle is not None:
            if hare == turtle:
                return True
            if hare is None or hare.next is None or hare.next.next is None:
                return False
            else:
                hare = hare.next.next

            turtle = turtle.next
        return False

if __name__ == '__main__':
    fourth = ListNode(-4)
    third = ListNode(0, fourth)
    second = ListNode(2, third)
    first = ListNode(1, second)
    print(Solution().hasCycle(first))
