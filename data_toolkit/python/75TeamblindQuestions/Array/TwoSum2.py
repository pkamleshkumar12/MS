from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        my_dict = {}
        for num in range(len(nums)):
            if nums[num] in my_dict:
                return [num, my_dict[nums[num]]]

            my_dict[target - nums[num]] = num


if __name__ == '__main__':
    # print(Solution().twoSum([2, 7, 11, 15], 9))
    # print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([2, 5, 5, 11], 10))
