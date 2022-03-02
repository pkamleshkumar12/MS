from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            f_flag = 0
            l_flag = 1
            min_height = height[f_flag] if height[f_flag] < height[l_flag] else height[l_flag]
            max_area = min_height * (l_flag - f_flag)
            return max_area

        f_flag = 0
        l_flag = len(height) - 1

        min_height = height[f_flag] if height[f_flag] < height[l_flag] else height[l_flag]
        max_area = min_height * (l_flag - f_flag)

        while f_flag < l_flag:
            if height[f_flag] > height[l_flag]:
                l_flag = l_flag - 1
            else:
                f_flag = f_flag + 1
            min_height = height[f_flag] if height[f_flag] < height[l_flag] else height[l_flag]
            new_max_area = min_height * (l_flag - f_flag)
            max_area = max(new_max_area, max_area)

        return max_area


if __name__ == '__main__':
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [2, 3, 4, 5, 18, 17, 6]
    print(Solution().maxArea(height))
