"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        start = 0
        last = 1
        while start < len(nums) -1:
            while last < len(nums):
                if nums[start] + nums[last] == target:
                    return [start, last]
                else:
                    last += 1
            start += 1
            last = start + 1


if __name__ == '__main__':
    # print(Solution().twoSum([2, 7, 11, 15], 9))
    # print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([2, 5, 5, 11], 10))
