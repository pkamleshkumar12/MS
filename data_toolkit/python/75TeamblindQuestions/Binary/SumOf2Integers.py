"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


# https://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a, b = (a ^ b), (a & b) << 1
        return a


if __name__ == '__main__':
    print(Solution().getSum(2147483647, 2))
