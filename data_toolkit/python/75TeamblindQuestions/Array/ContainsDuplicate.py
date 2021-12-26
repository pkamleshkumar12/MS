from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for i in range(len(nums)):
            if nums[i] in my_dict:
                return True
            else:
                my_dict[nums[i]] = i

        return False



if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 4, 1]))
