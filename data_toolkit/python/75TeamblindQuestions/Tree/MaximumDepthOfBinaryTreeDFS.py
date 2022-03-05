from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative solution - DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.rigth, depth + 1])

        return res
