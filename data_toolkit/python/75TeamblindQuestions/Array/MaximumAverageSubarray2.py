"""
You are given an integer array nums consisting of n elements, and
an integer k

"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_total = total
        l = 0
        for i in range(k, len(nums)):
            total = total + nums[i] - nums[l]
            max_total = max(total, max_total)
            l +=1
        return max_total/k


if __name__ == '__main__':
    arr = [0, 4, 0, 3, 2]
    print(Solution().findMaxAverage(arr, 1))
